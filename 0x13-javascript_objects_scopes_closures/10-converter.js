#!/usr/bin/node

exports.converter = function (base) {
  function convert (num) {
    const digits = '0123456789ABCDEF';

    if (num < base) {
      return digits[num];
    }

    return convert(Math.floor(num / base)) + digits[num % base];
  }

  return convert;
};
