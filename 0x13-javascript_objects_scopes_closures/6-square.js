#!/usr/bin/node
const Square0 = require('./5-square');
class Square extends Square0 {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
