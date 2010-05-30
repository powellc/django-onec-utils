from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings
from django import forms
from django.db.models import get_model
from django.utils import simplejson
from django.utils.safestring import mark_safe

from tagging.models import Tag
from recaptcha.client import captcha

class ReCaptcha(forms.widgets.Widget):
    recaptcha_challenge_name = 'recaptcha_challenge_field'
    recaptcha_response_name = 'recaptcha_response_field'

    def render(self, name, value, attrs=None):
        return mark_safe(u'%s' % captcha.displayhtml(settings.RECAPTCHA_PUBLIC_KEY))

    def value_from_datadict(self, data, files, name):
        return [data.get(self.recaptcha_challenge_name, None), 
            data.get(self.recaptcha_response_name, None)]
            


 
def MakeAutoCompleteTagInput(tagged_object):
    class AutoCompleteTagInput(forms.TextInput):
        class Media:
            css = {
                'all': ('jquery.autocomplete.css',)
            }
            js = (
                'js/jquery.js',
                'js/jquery.bgiframe.min.js',
                'js/jquery.ajaxQueue.js',
                'js/jquery.autocomplete.js'
            )
    
        def render(self, name, value, attrs=None):
            output = super(AutoCompleteTagInput, self).render(name, value, attrs)
            page_tags = Tag.objects.usage_for_model(tagged_object)
            tag_list = simplejson.dumps([tag.name for tag in page_tags],
                                        ensure_ascii=False)
            return output + mark_safe(u'''<script type="text/javascript">
                jQuery("#id_%s").autocomplete(%s, {
                    width: 150,
                    max: 10,
                    highlight: false,
                    multiple: true,
                    multipleSeparator: ", ",
                    scroll: true,
                    scrollHeight: 300,
                    matchContains: true,
                    autoFill: true,
                });
                </script>''' % (name, tag_list))