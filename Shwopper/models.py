from django.db import models
from decimal import Decimal
import datetime
from django.utils.timezone import utc
from accounts.models import MyProfile



#This class is used to represent a currency field in the database
class CurrencyField(models.DecimalField):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        try:
            return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
            return None


# This model holds all the affiliated links with the other attributes shown
class ShwopLink(models.Model):
    shwoplinkid = models.AutoField(primary_key=True)
    originallink = models.CharField("Original Link", max_length=1000)
    affiliatelink = models.CharField("Affiliate Link", max_length=1000, blank=True) #If blank means no affiliate link exists
    datecreated = models.DateTimeField("Date created", default=datetime.datetime.utcnow().replace(tzinfo=utc))
    visitcount = models.IntegerField("Visit count", default=0)
    userref = models.ForeignKey(MyProfile, verbose_name="User Profile", related_name="shwoplink", null=True, blank=True)

    def __unicode__(self):
        if self.affiliatelink:
            return self.affiliatelink
        return self.originallink

class AffiliatePayment(models.Model):
    affiliatepaymentid = models.AutoField(primary_key=True)
    shwoplinkref = models.ForeignKey(ShwopLink, verbose_name="Shwop Link Reference")
    amount = CurrencyField("Amount", decimal_places=2, max_digits=10)
    date = models.DateTimeField("Date of Payment", default=datetime.datetime.utcnow().replace(tzinfo=utc))
    userref = models.ForeignKey(MyProfile, verbose_name="User Profile", related_name="affiliatepayment", null=True, blank=True)

class PaymentToUser(models.Model):
    paymenttouserid = models.AutoField(primary_key=True)
    affiliatepaymentref = models.OneToOneField(AffiliatePayment, verbose_name="Affiliate Payment Reference")
    amount = CurrencyField("Amount", decimal_places=2, max_digits=10)
    date = models.DateTimeField("Date of Payment", default=datetime.datetime.utcnow().replace(tzinfo=utc))
    userref = models.ForeignKey(MyProfile, verbose_name="User Profile", related_name="paymenttouser")