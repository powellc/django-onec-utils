import re
from django_inlines.inlines import TemplateInline

class GMapInline(TemplateInline):
    """
    An inline that takes a gmap URL and returns the proper embed.

    Examples::

    {{ gmap http://maps.google.com/maps?f=q&source=s_q&hl=en&q=Mt+Canlaon,+Western+Visayas,+Philippines&aq=&sll=10.367439,123.206005&sspn=0.06062,0.110378&ie=UTF8&geocode=FdzCngAdnxBXBw&split=0&hq=&hnear=Mt+Canlaon&ll=10.833306,125.639648&spn=16.518845,28.256836&t=h&z=5 }}
   
    """
    help_text = "Takes a google maps URL or search string (with dashes for spaces)"

    inline_args = [
            dict(name='height', help_text="In pixels"),
            dict(name='width', help_text="In pixels"),
    ]
    def get_context(self):
        url = self.value
        return { 'url': url}
