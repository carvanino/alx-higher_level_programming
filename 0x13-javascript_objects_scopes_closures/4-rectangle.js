#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rectRep = '';
      for (let j = 0; j < this.width; j++) {
        rectRep = rectRep + 'X';
      }
      console.log(rectRep);
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    const multiple = 2;
    this.width = this.width * multiple;
    this.height = this.height * multiple;
  }
}

module.exports = Rectangle;
