#!/usr/bin/node
/* task 4
    Write an empty class Rectangle that defines a rectangle:

    Create an instance method called rotate() that exchanges the width and the height of the rectangle
    Create an instance method called double() that multiples the width and the height of the rectangle by 2
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

  rotate () {
    const aux = this.height;
    this.height = this.width;
    this.width = aux;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
