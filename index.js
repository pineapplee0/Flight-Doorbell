const homeCoords = require('./config.json').homeCoords;
const altThresh = 10000;
const distThresh = 10;
const trackedAircraft = require('./flights.json');
const notifyOnReg = [ "N500WR", "N714CB", "N5552E", "N385HA", "N178FA", "N409WN" ];

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin, 
  output: process.stdout,
  terminal: false
});


function meetsCriteria(aircraft) {
  let distance = distFrom(aircraft);
  let isSpecial =
    notifyOnReg.includes(aircraft.registration) &&
    aircraft.altitude <= altThresh &&
    distance <= distThresh;
  return isSpecial ? distance : false
}

rl.on('line', (line) => {
  console.log('hello world');
  console.log(line.split(","));
  let distance = meetsCriteria(currentAircraft)
  if (distance) {
    console.log(`Important plane detected ${distance} km away! Registration: ${currentAircraft.registration}`);
  } 
});

rl.on('close', () => {
  console.log('closed')
})

function distFrom(aircraft) {
  var homeLat = homeCoords[0]
  var homeLon = homeCoords[1]
  var lat = aircraft.coordinatePair[0];
  var lon = aircraft.coordinatePair[1];
  var R = 6371; // km
  var dLat = toRad(lat-homeLat);
  var dLon = toRad(lon-homeLon);
  var lat1 = toRad(homeLat);
  var lat2 = toRad(lat);

  var a = Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.sin(dLon/2) * Math.sin(dLon/2) * Math.cos(lat1) * Math.cos(lat2);
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  var d = R * c;
  return d.toFixed(1);
}
function toRad(Value)
{
  return Value * Math.PI / 180;
}
