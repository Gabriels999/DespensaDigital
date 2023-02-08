from django.contrib import admin

from core.models import ActivityLog, Product


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'target_quantity', 'real_quantity', 'type')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Product, ProductAdmin)
