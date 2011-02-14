from django.db import models
from decimal import Decimal
class CurrencyField(models.DecimalField):
    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        try:
           return super(CurrencyField, self).to_python(value).quantize(Decimal("0.01"))
        except AttributeError:
           return None

class USZipcodeField(models.CharField):
    ''' US Zipcode Field

    A really simple field that just makes sure to pad US zipcodes with zeros if needed.
    '''
    def __unicode__(self):
        return self.rjust(5, '0')

