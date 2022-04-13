const { homeCoords, favorites } = require('./config.json');
const altThresh = 10000;
const distThresh = 10;

const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin, 
  output: process.stdout,
  terminal: false
});


function checkAircraft(aircraft) {
  let distance = distFrom(aircraft);
  let isSpecial = favorites.filter(group => {
    return group.airframes.includes(aircraft.aircraftId)
  }).length != 0 &&
  aircraft.altitude <= altThresh &&
  distance <= distThresh;

  console.log(`Testing aircraft: ${JSON.stringify(aircraft)}`);

  if (isSpecial) {
    console.log(`Important plane detected ${distance} km away! Aircraft ID: ${aircraft.aircraftId}`);
  }
}

rl.on('line', (line) => {
  const msg = line.split(",");
  checkAircraft({
    coordinatePair: [msg[14], msg[15]],
    altitude: msg[11],
    aircraftId: msg[4]
  });
});

rl.on('close', () => {
  console.log('closed')
});

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
