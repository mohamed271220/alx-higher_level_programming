#!/usr/bin/node

const SqureBase = require('./5-square');

class Squre extends SqureBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Squre;
