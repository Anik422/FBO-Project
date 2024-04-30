from typing import Iterable, List
from django.db import models
from users.models import CustomUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from datetime import timedelta
import hashlib
import secrets

class MembershipServices(models.Model):
    name: str = models.CharField(max_length=100, db_index=True)
    slug: str = models.SlugField(max_length=100, db_index=True, unique=True)
    description: str = models.TextField(null=True, blank=True)
    created_at: str = models.DateTimeField(auto_now_add=True)
    updated_at: str = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Membership Service"
        verbose_name_plural = "Membership Services"
        ordering = ["id"]

    # slug auto generation
    def save(self, *args, **kwargs) -> None:
        self.slug: str = self.slug or slugify(self.name)
        super().save(*args, **kwargs)


class MembershipPlans(models.Model):
    name: str = models.CharField(max_length=100, db_index=True)
    slug: str = models.SlugField(max_length=100, db_index=True, unique=True)
    description: str = models.TextField(null=True, blank=True)
    price: float = models.FloatField(default=0.0)
    access_to_services: Iterable[MembershipServices] = models.ManyToManyField(
        MembershipServices
    )
    created_at: str = models.DateTimeField(auto_now_add=True)
    updated_at: str = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs) -> None:
        self.slug: str = self.slug or slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name: str = "Membership Plan"
        verbose_name_plural: str = "Membership Plans"
        ordering: List[str] = ["created_at"]


class Pricing(models.Model):
    PACKAGE_OPTIONS = (
        ("monthly", _("Monthly")),
        ("quarterly", _("Quarterly")),
        ("half_yearly", _("Half Yearly")),
        ("yearly", _("Yearly")),
    )
    membership_plan: Iterable[MembershipPlans] = models.ForeignKey(
        MembershipPlans, on_delete=models.CASCADE, verbose_name="Membership Plan"
    )
    package: str = models.CharField(
        max_length=20,
        choices=PACKAGE_OPTIONS,
        default="monthly",
        verbose_name="Package",
    )
    days: int = models.IntegerField(default=30, verbose_name="Days")
    price: float = models.FloatField(default=0.0, verbose_name="Price")
    created_at: str = models.DateTimeField(auto_now_add=True)
    updated_at: str = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.membership_plan} - {self.package} - {self.price}"

    class Meta:
        verbose_name: str = "Pricing"
        verbose_name_plural: str = "Pricings"
        ordering: List[str] = ["created_at"]


class SubscriptionPlan(models.Model):
    membership_plan = models.ForeignKey(MembershipPlans, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    pricing = models.ForeignKey(Pricing, on_delete=models.CASCADE, null=True, blank=True)
    number_of_people = models.IntegerField(verbose_name="Number of People", default=1)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def generate_unique_id(self) -> str:
        unique_id = secrets.token_hex(5)  # Generate a random hex string of 10 characters
        return unique_id

    def encrypt_id(self, unique_id: str) -> str:
        # Encrypt the unique ID using hashlib
        encrypted_id = hashlib.sha256(unique_id.encode()).hexdigest()
        return encrypted_id

    @property
    def subscription_id(self) -> str:
        unique_id = self.generate_unique_id()
        encrypted_id = self.encrypt_id(unique_id)
        return encrypted_id[:10]  # Return the first 10 characters of the encrypted ID

    def __str__(self):
        return f"{self.user} - {self.membership_plan}"
    

    def save(self, *args, **kwargs):
        if not self.subscription_id:
            self.subscription_id = self.generate_unique_id()
        if self.pricing and not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.pricing.days)
        super().save(*args, **kwargs)