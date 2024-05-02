from django.contrib import admin
from .models import MembershipServices, MembershipPlans, SubscriptionPlan, Pricing


class MembershipServicesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at", "updated_at")
    list_display_links = (
        "id",
        "name",
    )
    prepopulated_fields = {"slug": ("name",)}


class MembershipPlansAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "price", "created_at", "updated_at")
    list_display_links = ("id", "name", "price")
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("access_to_services",)


class SubscriptionPlanAdmin(admin.ModelAdmin):
    list_display = ("subscription_id", "membership_plan", "user", "pricing", "number_of_people", "active")
    list_display_links = ("subscription_id", "membership_plan", "user", "pricing", "number_of_people", "active")
    list_filter = ("membership_plan", "pricing", "active")



class PricingAdmin(admin.ModelAdmin):
    list_display = ("membership_plan", "package", "price", "created_at", "updated_at")
    list_display_links = ("membership_plan", "package", "price")
    list_filter = ("membership_plan", "package")


admin.site.register(MembershipServices, MembershipServicesAdmin)
admin.site.register(MembershipPlans, MembershipPlansAdmin)
admin.site.register(SubscriptionPlan, SubscriptionPlanAdmin)
admin.site.register(Pricing, PricingAdmin)
