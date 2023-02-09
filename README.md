# Flight-Doorbell
A physical alert method for plane spotting. Flight Doorbell is a program that you run on a Raspberry Pi to ensure that you recieve an alert for your favorite aircrafts right from your desk, bedroom, living area, etc. 

As a self proclaimed "avgeek", I'm constantly on FlightRadar24 browsing for specific airlines, registrations, or aircraft types. Being near the approach path for 18R/L and departure path for 36L/R, I never miss an opportunity to run outside and see some of my favorite planes. While FlightRadar24 is a good, affordable resource, it lacks a lot of information. A lot of delayed information, lack of SOME military or general aviation aircraft, and glitched planes on the map, to name a few. Using an SDR to track aircrafts via ADSB, I'm able to monitor every plane within the airspace accurately (even those who choose not to be displayed on FR24 or other flight tracking resources). 


# Why Flight Doorbell? 

While FlightRadar24 is a fairly accessible source that includes a push notification system, I've found their notifications to be somewhat unreliable. I'm either not notified in time or sometimes I'm not even notified at ALL when my favorite Southwest special happens to be in town. While there is a way to have FlightRadar24 send me a push notification whenever an aircraft is within the AUS airspace, Flight Doorbell is designed to eliminate any chances of misinterupted data. Flight Doorbell sends you a physical notification via blinking lights that coorespond to the airline and a fasten seatbelt chime that will be far too flashy to go ignored.

Originally, I had planned on using FlightAware's API for Flight Doorbell. One of the problems I encountered with FlightAware's API was the constant rate limiting during my early testing phases, thus resulting in my card being charged. As a result, I created Flight Doorbell to eliminate the usage of using a subscription based API. 

# How to set up Flight Doorbell

This section is coming soon!

# Parts List

Part Name                           | Price  | Where to Buy
------------------------------------|--------|---------------------------
Antenna - female connector, 26 inch | $44.95 | [Amazon](https://www.amazon.com/ADSBexchange-5-5dBi-N-Type-Female-Antenna/dp/B089Q4BVCB?pd_rd_w=AZgzG&pf_rd_p=8e4731a7-b756-4530-8014-2f681a6d39bb&pf_rd_r=DQSPVY4J7XR1PRR0AQN2&pd_rd_r=071d9d5d-8bc0-429f-82f5-0dfbb8c1b062&pd_rd_wg=3GJbW&pd_rd_i=B089Q4BVCB&psc=1&ref_=pd_bap_d_rp_6_i)
Antenna extension cable - male, 49ft | $19.70 | [Amazon](https://www.amazon.com/YOTENKO-Connector-Pigtail-Antenna-Arrester/dp/B07T6LVRXY?pd_rd_w=AZgzG&pf_rd_p=8e4731a7-b756-4530-8014-2f681a6d39bb&pf_rd_r=DQSPVY4J7XR1PRR0AQN2&pd_rd_r=071d9d5d-8bc0-429f-82f5-0dfbb8c1b062&pd_rd_wg=3GJbW&pd_rd_i=B07T6LVRXY&psc=1&ref_=pd_bap_d_rp_4_t)
Coaxial antenna adapter - SMA female to MCX male | $9.70 | [Amazon](https://www.amazon.com/YOTENKO-Connector-Pigtail-Antenna-Arrester/dp/B07T6LVRXY?pd_rd_w=AZgzG&pf_rd_p=8e4731a7-b756-4530-8014-2f681a6d39bb&pf_rd_r=DQSPVY4J7XR1PRR0AQN2&pd_rd_r=071d9d5d-8bc0-429f-82f5-0dfbb8c1b062&pd_rd_wg=3GJbW&pd_rd_i=B07T6LVRXY&psc=1&ref_=pd_bap_d_rp_4_t)
SDR - Realtek, RTL2832U | $22.95 | [Amazon](https://www.amazon.com/RioRand-Receiver-Low-Cost-Software-Defined/dp/B00UAB79WG)
Raspberry Pi - 2b+ | $35 | [RaspberryPi](https://www.raspberrypi.com/products/raspberry-pi-1-model-b-plus/)
RGB LED - OSEPP, 10 pack | $3.50 | [OSEPP](https://www.osepp.com/accessories/components/159-ls-00043-rgb-tri-color-10mm-led)
Electrolytic capacitor - 10uF | $1.32/4 | [Mouser](https://www.mouser.com/ProductDetail/Nichicon/UVZ1C100MDD1TD?qs=Wj11ghCn0FlmE%252BCwJNjfQQ%3D%3D&countrycode=US&currencycode=USD)
Polyester film capacitor - 0.01uF | $1.64/4 | [Mouser](https://www.mouser.com/ProductDetail/Nichicon/QYX2A103JTP?qs=p6VZ%252BklCkRS7UlSQfXalkg%3D%3D&countrycode=US&currencycode=USD)
Assorted resistors - Bojack 100 pc | $14 | [Amazon](https://www.amazon.com/BOJACK-Values-Resistor-Resistors-Assortment/dp/B08FHPKF9V/ref=sr_1_3?crid=NSDCU4RXET6H&keywords=bojack%2Bresistor%2Bkit&qid=1675982609&sprefix=%2Caps%2C98&sr=8-3&th=1)
Perfboards - copper, 20pc | $6.79 | [Amazon](https://www.amazon.com/Perfboard-Composite-Breadboard-Prototyping-Electronic/dp/B072Q1H6GX/ref=sr_1_3?crid=3CVHLVNQZD6E2&keywords=copper+perfboard&qid=1675982670&sprefix=copper+perfboar%2Caps%2C127&sr=8-3)
Total | ~ $157.33
