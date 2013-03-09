from django.contrib import admin
from Shwopper.models import ShwopLink, AffiliatePayment, PaymentToUser

class ShwopLinkAdmin(admin.ModelAdmin):
    fields = ['originallink', 'affiliatelink', 'datecreated', 'visitcount', 'userref']

    #Comment this if you would like to make the fields editable
    readonly_fields = ['originallink','affiliatelink', 'datecreated', 'visitcount', 'userref']

    list_display = ['shwoplinkid', 'originallink', 'affiliatelink', 'datecreated', 'visitcount', 'userref']
    ordering = ('shwoplinkid',)

admin.site.register(ShwopLink, ShwopLinkAdmin)
admin.site.register(AffiliatePayment)
admin.site.register(PaymentToUser)
