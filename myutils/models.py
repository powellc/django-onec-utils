from datetime import *
from django.db import models
from django.utils.translation import ugettext_lazy as _

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
    #	self.deleted=True
    #	super(StandardMetadata, self).delete(*args, **kwargs)
