from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode
from users.tokens import account_activation_token
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from urllib.parse import urlparse, urlunparse

def is_safe_url(url, allowed_hosts):
    """
    Return True if the url is a safe redirect. Safe redirects are either:
      - The same host as the current host
      - A relative URL
      - A scheme-relative URL (e.g. '//example.com')
    """
    parsed_url = urlparse(url)
    return (
        not parsed_url.netloc or
        parsed_url.netloc == allowed_hosts or
        parsed_url.netloc == '' and urlunparse(parsed_url) == urlunparse(urlparse(urlunparse(url)._replace(netloc=allowed_hosts)))
    )



def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string(
        template_name="users/activate_account.html",
        context={
            "user": user.username,
            "domain": get_current_site(request).domain,
            "uid": urlsafe_base64_encode(force_bytes(user.pk)),
            "token": account_activation_token.make_token(user),
            "protocol": "https" if request.is_secure() else "http",
        },
        request=request,
    )
    email = send_mail(subject=mail_subject, message=message, from_email="info@trademajestic.com", recipient_list=[to_email])
    if email == 1:
        messages.success(
            request,
            f"Dear <b>{user.first_name}</b>, place go to you email <b>{to_email}</b> inbox and click on received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder if you don't see the email in your inbox.",
        )
    else:
        messages.error(
            request,
            f"Problem sending email to {to_email}, check if you typed it correctly.",
        )
