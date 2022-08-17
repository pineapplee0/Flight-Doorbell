#library imports
import sys
import json
import datetime
import math

#store credentials as var
import config

for line in sys.stdin

def checkAircraft(aircraft):
    distance = distFrom(aircraft);
    matches = favorites.filter #finish off the rest of this line
    return airframes in aircraft.aircraftId
    isSpecial = 
        len(matches) != 0 and
        aircraft.altitude <= thresholds.altitude and
        distance <= thresholds.distance

print(f'Testing aircraft: {json.dumps(aircraft)}');
print(recentAircraft); 

if (isSpecial):
    print(f'Important plane detected {distance} km away! Aircraft ID: {aircraft.aircraftId}. Group colors: {matches[0].colors}');

def distFrom(aircraft):
    R = 6371 # earth radius in km
    homeLat = config.homeCoords[0]
    homeLon = config.homeCoords[1]
    lat = aircraft.coordinatePair[0]
    lon = aircraft.coordinatePair[1]
    dlat = toRad(lat-homeLat)
    dLon = toRad(lon-homeLon)
    lat1 = toRad(homeLat)
    lat2 = toRad()

    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return round(d, 1)

def toRad(value):
    return value * math.pi / 180 
