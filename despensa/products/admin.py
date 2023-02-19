from django.contrib import admin

from .models import ActivityLog, Product, UserStore


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'type')


class UserStoreAdmin(admin.ModelAdmin):
    list_display = ('owner', 'product', 'target_quantity', 'real_quantity')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(UserStore, UserStoreAdmin)
