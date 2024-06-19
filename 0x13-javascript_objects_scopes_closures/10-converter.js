#!/usr/bin/node

function converter (base) {
  function convertToBase (number) {
    if (number === 0) {
      return '';
    } else {
      let remainder = number % base;
      let quotient = Math.floor(number / base);
      if (remainder < 10) {
        return convertToBase(quotient) + remainder;
      } else {
        return convertToBase(quotient) + String.fromCharCode(remainder + 55);
      }
    }
  }

  return convertToBase;
}

module.exports.converter = converter;
