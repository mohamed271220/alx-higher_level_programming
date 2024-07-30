#!/usr/bin/node
// Star Wars Characters

const request = require('request');
const util = require('util');
const requestPromise = util.promisify(request.get); // Convert callback-based request.get to return a Promise
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, async (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const content = JSON.parse(body);
  const characters = content.characters;

  const characterPromises = characters.map(character => requestPromise(character, { json: true }));

  try {
    const responses = await Promise.all(characterPromises);
    responses.forEach(res => console.log(res.body.name));
  } catch (error) {
    console.log(error);
  }
});
