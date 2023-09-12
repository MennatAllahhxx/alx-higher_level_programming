#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let index = 0; index < size; index++) {
      console.log(c.repeat(size));
    }
  }
}
module.exports = Square;
