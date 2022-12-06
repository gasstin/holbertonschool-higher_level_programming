#!/usr/bin/node
/* task 3
    Write an empty class Rectangle that defines a rectangle:

    Create an instance method called print() that prints the rectangle using the character X
*/

class Rectangle {
  constructor (w, h) {
    if ((w > 0) & (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let lineToPrint = '';
    for (let index = 0; index < this.width; index++) {
      lineToPrint += 'X';
    }
    for (let index = 0; index < this.height; index++) {
      console.log(lineToPrint);
    }
  }
}

module.exports = Rectangle;
