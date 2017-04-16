# author Maha Alidrisi - p12
import urllib2
import urllib
import json
import math

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
address = raw_input('Please enter location: ')

if len(address) < 1 or "hoboken" in address:
    print "Please enter a location or non-Hoboken city!"
else:
    url = serviceurl + urllib.urlencode({"sensor": "false", "address": address})
    request = urllib2.Request(url,headers={'User-Agent': 'Safari/537.36'})
    try:
        data = urllib2.urlopen(request).read().decode()
        js = json.loads(data)
    except:
        js = None
        print "Please enter a valid location"
    else:
        if "status" not in js or js["status"] != "OK":
            print "The distance can no be calculated"
        else:
            lat1= 40.7439905
            lon1= -74.0323626
            lat2 = js["results"][0]["geometry"]["location"]["lat"]
            lon2 = js["results"][0]["geometry"]["location"]["lng"]
            location = js["results"][0]["formatted_address"]
            dlat = math.radians(lat2-lat1)
            dlon = math.radians(lon2-lon1)
            radius = 3956
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1))* math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = radius * c
            print "The distance between Hoboken, NJ and", address," is approximately", int(round(d)), "miles"

