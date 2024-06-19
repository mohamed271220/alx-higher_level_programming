#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const key in dict) {
  const occCount = dict[key];
  if (newDict[occCount] === undefined) {
    newDict[occCount] = [];
  }
  newDict[occCount].push(key);
}

console.log(newDict);
