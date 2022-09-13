#library imports
from playsound import playsound
import sys
import json
import datetime
import math

#store credentials as variable
import config

#create recentAircraft object
recentAircraft = {}

#calculating distance of aircraft from homeCoords in km
def distFrom(aircraft):
    R = 6371 # earth radius in km
    homeLat = config.homeCoords[0]
    homeLon = config.homeCoords[1]
    lat = aircraft['coordinatePair'][0]
    lon = aircraft['coordinatePair'][1]
    dLat = toRad(lat-homeLat)
    dLon = toRad(lon-homeLon)
    lat1 = toRad(homeLat)
    lat2 = toRad(lat)

    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.sin(dLon / 2) * math.sin(dLon / 2) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return round(d, 1)

def toRad(value):
    return value * math.pi / 180 

def checkAircraft(aircraft):
    distance = distFrom(aircraft);
    matches = list(filter(lambda group: aircraft['aircraftId'] in group['airframes'], config.favorites))
    isSpecial = len(matches) != 0 and aircraft['altitude'] <= config.thresholds['altitude'] and distance <= config.thresholds['distance']
    print(f"Testing aircraft: {json.dumps(aircraft)}");
    if (isSpecial):
        print(f"Important plane detected {distance} km away! Aircraft ID: {aircraft['aircraftId']}. Group colors: {matches[0]['colors']}");
        playsound('assets/chime.wav')

for line in sys.stdin:
    msg = line.split(",")
    if (msg[4] and msg[11] and msg[14] and msg[15]):
        recentAircraft[msg[4]] = datetime.datetime.now()
        timeDiff = recentAircraft[msg[4]] - datetime.datetime.now()
        if timeDiff.total_seconds() >= 3:
            print("deleting... {msg[4]}")
            del recentAircraft[4]
        checkAircraft({'coordinatePair': [float(msg[14]), float(msg[15])], 'altitude': float(msg[11]), 'aircraftId': msg[4]})
