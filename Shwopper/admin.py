from django.contrib import admin
from Shwopper.models import ShwopLink, Transaction

class ShwopLinkAdmin(admin.ModelAdmin):
    fields = ['shwoplink', 'datecreated', 'visitcount', 'isaffiliate']

    #Comment this if you would like to make the fields editable
    readonly_fields = ['shwoplink', 'datecreated', 'visitcount', 'isaffiliate']

    list_display = ['shwoplinkid', 'shwoplink', 'datecreated', 'visitcount', 'isaffiliate']
    ordering = ('shwoplinkid',)

admin.site.register(ShwopLink, ShwopLinkAdmin)
admin.site.register(Transaction)