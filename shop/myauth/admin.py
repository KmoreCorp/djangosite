from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import NonVipUser
# Register your models here.

class NonVipUserInline(admin.TabularInline):
    model = NonVipUser
    can_delete = False
    verbose_name = '普通会员'
    verbose_name_plural = '普通会员'

class UserAdmin(BaseUserAdmin):
    """自定义新样式"""
    inlines = (NonVipUserInline, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
