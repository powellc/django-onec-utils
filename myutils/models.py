from datetime import *
import random, string
import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us.models import USStateField, PhoneNumberField
from django.contrib.markup.templatetags import markup

from myutils.fields import USZipcodeField
from myutils.utils import google_lat_long

MARKUP_HTML = 'h'
MARKUP_MARKDOWN = 'm'
MARKUP_REST = 'r'
MARKUP_TEXTILE = 't'
MARKUP_OPTIONS = getattr(settings, 'MARKUP_OPTIONS', (
        (MARKUP_HTML, _('HTML/Plain Text')),
        (MARKUP_MARKDOWN, _('Markdown')),
        (MARKUP_REST, _('ReStructured Text')),
        (MARKUP_TEXTILE, _('Textile'))
    ))
MARKUP_DEFAULT = getattr(settings, 'MARKUP_DEFAULT', MARKUP_MARKDOWN)

MARKUP_HELP = _("""Select the type of markup you are using in this article.
<ul>
<li><a href="http://daringfireball.net/projects/markdown/basics" target="_blank">Markdown Guide</a></li>
<li><a href="http://docutils.sourceforge.net/docs/user/rst/quickref.html" target="_blank">ReStructured Text Guide</a></li>
<li><a href="http://thresholdstate.com/articles/4312/the-textile-reference-manual" target="_blank">Textile Guide</a></li>
</ul>""")

class MarkupMixin(models.Model):
    markup = models.CharField(max_length=1, choices=MARKUP_OPTIONS, default=MARKUP_DEFAULT, help_text=MARKUP_HELP)

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        #self.do_render_markup()
        super(MarkupMixin, self).save(*args, **kwargs)

    def do_render_markup(self):
        """Turns any markup into HTML"""

        original = self.rendered_content
        if self.markup == MARKUP_MARKDOWN:
            self.rendered_content = markup.markdown(self.content)
        elif self.markup == MARKUP_REST:
            self.rendered_content = markup.restructuredtext(self.content)
        elif self.markup == MARKUP_TEXTILE:
            self.rendered_content = markup.textile(self.content)
        else:
            self.rendered_content = self.content

        return (self.rendered_content != original)


class USAddressPhoneMixin(models.Model):
    """
    Mixin that handles models that need to have an address associated with it.

    Note: This is none to sophisticated and would need some fleshing out for int'l applications.

    Also, a little trick where it looks up a lat long using google...
    """

    address=models.CharField(_('Address'), max_length=255)
    town=models.CharField(_('Town'), max_length=100)
    state=USStateField(_('State'))
    zipcode=USZipcodeField(_('Zip'), max_length=5)
    phone=PhoneNumberField(_('phone'), blank=True, null=True)
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
        super(USAddressPhoneMixin, self).save(*args, **kwargs)


try:
    RAND_FIELD_LENGTH=settings.RAND_FIELD_LENGTH
except:
    RAND_FIELD_LENGTH = 8

class RandomIDMixin(models.Model):
    """
    Taken directly from djangosnippet.org/snippets/814/
    """
    id = models.CharField(primary_key=True, max_length=RAND_FIELD_LENGTH)
    
    def save(self):
        if not self.id:
            self.id = random_id(RAND_FIELD_LENGTH)
            super(RandomIDMixin, self).save()
    
    class Meta:
        abstract = True
    
    # alphabet will become our base-32 character set:
    alphabet = string.lowercase + string.digits 
    # We must remove 4 characters from alphabet to make it 32 characters long. We want it to be 32
    # characters long so that we can use a whole number of random bits to index into it.
    for loser in 'l1o0': # Choose to remove ones that might be visually confusing
        i = alphabet.index(loser)
        alphabet = alphabet[:i] + alphabet[i+1:]
    
    def byte_to_base32_chr(byte):
        return alphabet[byte & 31]

    def random_id(length):
        # Can easily be converted to use secure random when available
        # see http://www.secureprogramming.com/?action=view&feature=recipes&recipeid=20
        random_bytes = [random.randint(0, 0xFF) for i in range(length)]
        return ''.join(map(byte_to_base32_chr, random_bytes))


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

