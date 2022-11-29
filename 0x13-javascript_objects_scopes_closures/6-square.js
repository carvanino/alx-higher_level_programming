#!/usr/bin/node
const Rectangle = require('./5-square');

class Square extends Rectangle {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let rectRep = '';
      for (let j = 0; j < this.width; j++) {
        if (typeof (c) === 'undefined') {
          rectRep = rectRep + 'X';
        } else {
          rectRep = rectRep + c;
        }
      }
      console.log(rectRep);
    }
  }
}

module.exports = Square;
