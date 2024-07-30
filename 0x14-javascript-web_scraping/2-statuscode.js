#!/usr/bin/node
// Status Of Get request

const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  error ? console.log(error) : console.log(`code: ${response.statusCode}`);
});
