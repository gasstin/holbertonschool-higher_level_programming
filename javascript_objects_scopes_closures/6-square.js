#!/usr/bin/node
/* task 6
Write a class Square that defines a square and inherits from Rectangle:

Create an instance method called charPrint(c) that prints the rectangle using the character c
If c is undefined, use the character X
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let lineToPrint = '';
    for (let index = 0; index < this.width; index++) {
      lineToPrint += c;
    }
    for (let index = 0; index < this.width; index++) {
      console.log(lineToPrint);
    }
  }
}

module.exports = Square;
