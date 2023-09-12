#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      const str = 'X';
      console.log(str.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
