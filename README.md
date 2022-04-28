# Flight-Doorbell
A physical alert method for plane spotting. Flight Doorbell is a program that you run on a Raspberry Pi to ensure that you recieve an alert for your favorite aircrafts right from your desk, bedroom, living area, etc. 

As a self proclaimed "avgeek", I'm constantly on FlightRadar24 browsing for specific airlines, registrations, or aircraft types. Being near the approach path for 18R/L and departure path for 36L/R, I never miss an opporunity to run outside and see some of my favorite planes. While FlightRadar24 is a good resource for those who don't want to spend a pretty penny, it lacks a lot of information. Delayed information, lack of SOME military or general aviation aircraft due to privacy reasons, and glitched planes on the map to name a few. Using an SDR to track aircrafts via ADSB, I'm able to monitor every plane within the airspace accurately (even those who choose not to be displayed on FR24 or other flight tracking resources). 


# Why Flight Doorbell? 

While FlightRadar24 is a fairly accessible source that includes a push notification system, I've found their notifications to be somewhat unreliable. I'm either not notified in time or sometimes I'm not even notified at all when my favorite Southwest special happens to be in town. While there is a way to have FlightRadar24 send me a push notification whenever an aircraft is within the AUS airspace, Flight Doorbell is designed to eliminate any chances of misinterupted data. Flight Doorbell sends you a physical notification via blinking lights that coorespond to the airline and a fasten seatbelt chime that will be far too flashy to go ignored. 

Originally, I had planned on using FlightAware's API for Flight Doorbell. One of the problems I encountered with FlightAware's API was the constant rate limiting during my early testing phases, thus resulting in my card being charged. As a result, I created Flight Doorbell to eliminate the usage of using a subscription based API. 

# How to set up Flight Doorbell

This section is coming soon.

# Parts List

- 5.5dBi 1090/978 N-Type Female Antenna 26 inch - $44.95
- YOTENKO 49.2Ft RG58 coaxial cable N male to SMA male connector low-loss antenna extension cable - $19.69
- DZS Elec 2pcs RG316 wire jumper 15cm SMA female to MCX male coaxial cable antenna adapter - $9.69
- Realtek RTL2832U SDR - $22.95
- Raspberry Pi 2b+ - $35
- OSEPP RGB 10mm LED (10 pack) - $3.49

Total ~ $135.77
