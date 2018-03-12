#!/usr/bin/python2.7

import math 

def Distance(lat2, lon2, lat1, lon1):
    R = 3959
    latitude1 = math.radians(lat1)
    latitude2 = math.radians(lat2)
    #longitude2 = math.radians(lon2)
    #longitude1 = math.radians(lon1)
    distlat = math.radians(latitude2-latitude1)
    distlong = math.radians(lon2-lon1)
    
    a = math.sin(distlat/2) * math.sin(distlat/2) + math.cos(latitude1) * math.cos(latitude2) * math.sin(distlong/2) * math.sin(distlong/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d
def distance(lat1, lon1,lat2,lon2):
    #lat1, lon1 = origin
    #lat2, lon2 = destination
    radius = 3959 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d


r =Distance (40.5, -73.99, 40.5, -73.98)
r1 =distance (40.5, -73.99, 40.5, -73.98)
print r,r1