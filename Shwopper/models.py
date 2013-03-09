from django.db import models
from decimal import Decimal
import datetime
from django.utils.timezone import utc



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
    shwoplink = models.CharField("Shwop Link", max_length=1000)
    datecreated = models.DateTimeField("Date created", default=datetime.datetime.utcnow().replace(tzinfo=utc))
    visitcount = models.IntegerField("Visit count", default=0)
    isaffiliate = models.BooleanField("Is an affiliate link")
    #userid = models.ForeignKey(User, verbose_name="User")

    def __unicode__(self):
        return self.shwoplink

class Transaction(models.Model):
    transactionid = models.AutoField(primary_key=True)
    shwoplink = models.ForeignKey(ShwopLink, verbose_name="Shwop Link")
    amount = CurrencyField("Amount", decimal_places=2, max_digits=10)
    domain = models.CharField("Domain", max_length=10)
    date = models.DateTimeField("Date", default=datetime.datetime.utcnow().replace(tzinfo=utc))
    paid = models.BooleanField("It has been paid")
    #userid = models.ForeignKey(User, verbose_name="User")