from datetime import *
import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from myutils.fields import USZipcodeField
from myutils.utils import google_lat_long

class USAddressModel(models.Model):
    """
    Handles models that need to have an address associated with it.

    Note: This is none to sophisticated and would need some fleshing out for int'l applications.

    Also, a little trick where it looks up a lat long using google...
    """

    address=models.CharField(_('Address'), max_length=255)
    town=models.CharField(_('Town'), max_length=100)
    state=USStateField(_('State'))
    zipcode=USZipcodeField(_('Zip'), max_length=5)
    lat_long=models.CharField(_('Coordinates'), max_length=255, blank=True, null=True)

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        if not self.lat_long:
            location = "%s +%s +%s +%s" % (self.address, self.town, self.state, self.zipcode)
            self.lat_long = google_lat_long(location)
            if not self.lat_long:
                location = "%s +%s +%s" % (self.town, self.state, self.zipcode)
                self.lat_long = google_lat_long(location)
        super(USAddressModel, self).save(*args, **kwargs)

class StandardMetadata(models.Model):
    """
    A basic (abstract) model for metadata.
    
    Included in each model file to maintain application separation.
    
    Subclass new models from 'StandardMetadata' instead of 'models.Model'.
    """
    created = models.DateTimeField(_('created'), default=datetime.now, editable=False)
    updated = models.DateTimeField(_('updated'), default=datetime.now, editable=False)
    #deleted = models.BooleanField(_('deleted'), default=False, editable=False)
        
    class Meta:
        abstract = True
        
    def save(self, *args, **kwargs):
        self.updated = datetime.now()
        super(StandardMetadata, self).save(*args, **kwargs)

    #def delete(self, *args, **kwargs):
    #   self.deleted=True
    #   super(StandardMetadata, self).delete(*args, **kwargs)
