import urllib.request
from xml.etree.ElementTree import parse
import webbrowser
import time

while True:
    u = urllib.request.urlopen("http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22")
    data = u.read()
    f = open("rt22.xml","wb")
    f.write(data)
    f.close()
    doc = parse("rt22.xml")

    halfmile_of_lat = 0.007246
    halfmile_of_lon = 0.008333
    office_lat = 41.98062
    office_lon = -87.668452
    lower_radius_lat = office_lat - halfmile_of_lat
    upper_radius_lat = office_lat + halfmile_of_lat
    left_radius_lon = office_lon - halfmile_of_lon
    right_radius_lon = office_lon + halfmile_of_lon

    doc = parse("rt22.xml")

    for bus in doc.findall('bus'):
        direction = bus.findtext("d")
        latitude = float(bus.findtext("lat"))
        longitude = float(bus.findtext("lon"))
        if direction == "North Bound":
            if latitude >= lower_radius_lat and latitude <= upper_radius_lat and longitude >= left_radius_lon and longitude <= right_radius_lon:
                webbrowser.open("https://www.google.com.ar/maps/@{},{},21z".format(latitude,longitude))

    time.sleep(30)



