from django.contrib import admin
from .models import UserAlerts, EbayItems


@admin.register(UserAlerts)
class UserAlertsAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    list_display = ('id', 'email', 'period', 'search_phrase')


@admin.register(EbayItems)
class EbayCardItemsAdmin(admin.ModelAdmin):
    fields = ('item_id', 'title', 'category_path', 'image_url', 'item_web_url', 'description',
              'category_id', 'created_at', 'updated_at')
    list_display = ('item_id', 'title',)
    list_filter = ('category_path', 'category_id')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at',)
