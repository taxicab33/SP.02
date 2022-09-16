from django.contrib import admin

from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email',
                    'first_name',
                    'surname',
                    'last_name',
                    'is_superuser',
                    'is_staff',
                    'role')
