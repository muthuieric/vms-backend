from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUserModel

# Register your models here.
class UserAdminCustom(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "role", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {"classes": ("wide",), "fields": ("email", "first_name", "last_name", "role", "password1", "password2"),},
        ),
    )
    list_display = ("email", "first_name", "last_name", "role",  "is_staff")
    search_fields = ("first_name", "last_name", "email","role", )
    ordering = ("email",)
    readonly_fields = ['date_joined', 'last_login']

admin.site.register(CustomUserModel, UserAdminCustom)