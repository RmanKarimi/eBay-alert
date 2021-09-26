from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserAlerts(models.Model):
    PERIOD = (
        ('2', '2 minutes'),
        ('10', '10 minutes'),
        ('20', '20 minutes')
    )
    email = models.EmailField(max_length=256, verbose_name=_('Email'))
    period = models.CharField(choices=PERIOD, max_length=30, default='20', verbose_name=_('Period'))
    search_phrase = models.CharField(max_length=256, verbose_name=_('Search Phrase'))
    create_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))
    update_date = models.DateTimeField(auto_now=True, verbose_name=_('Updated Date'))

    class Meta:
        verbose_name= _('User Alert')
        verbose_name_plural = _('User Alerts')

    def __str__(self):
        return self.email


class EbayItems(models.Model):
    user_alert = models.ForeignKey(UserAlerts, on_delete=models.CASCADE, verbose_name=_('User Alert'))
    item_id = models.CharField(blank=False, null=False, verbose_name=_('Item ID'), max_length=250)
    title = models.CharField(blank=False, null=False, verbose_name=_('Title'), max_length=1000)
    category_path = models.CharField(blank=False, null=False, verbose_name=_('Item ID'), max_length=250)
    image_url = models.URLField(blank=False, null=False, verbose_name=_('Image URL'), max_length=250)
    item_web_url = models.URLField(blank=False, null=False, verbose_name=_('Item URL'), max_length=250)
    description = models.TextField(null=False, blank=False, verbose_name=_('Description'))
    category_id = models.CharField(blank=False, null=False, verbose_name=_('Category ID'), max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_('Updated At'))
    value = models.DecimalField(decimal_places=3, max_digits=6, blank=False, default=0.0, verbose_name=_('Value'))
    currency = models.CharField(blank=False, null=False, verbose_name=_('Currency'), max_length=10)

    def __str__(self):
        return self.item_id

    class Meta:
        verbose_name = _('eBay Card Item')
        verbose_name_plural = _('eBay Card Items')


