#!/usr/bin/node
// Star Wars movie title using async/await

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, (err, res, body) => {
  err ? console.log(err) : console.log(JSON.parse(body).title);
});
