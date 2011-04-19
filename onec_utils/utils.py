import urllib
import settings
import logging

def google_lat_long(location):
    try:
        key=settings.GOOGLE_API_KEY
        output = "csv"
        location = urllib.quote_plus(location)
        logging.debug('myutils.utils: google_lat_long() says "Requesting lat/long from Google."')
        request = "http://maps.google.com/maps/geo?q=%s&output=%s&key=%s" % (location, output, key)
        data = urllib.urlopen(request).read()
        dlist = data.split(',')
        if dlist[0] == '200':
            coords = "%s, %s" % (dlist[2], dlist[3])
        else:
            coords = ''
    except:
        logging.debug('myutils.utils: google_lat_long() says "No Google API key set."')
        coords = ''
    return coords
