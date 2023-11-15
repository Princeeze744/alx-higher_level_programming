#!/usr/bin/node
const object = require('./5-square');

class Square extends object {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let printSquare = '';
      for (let j = 0; j < this.width; j++) {
        printSquare = printSquare + c;
      }
      console.log(printSquare);
    }
  }
}
module.exports = Square;
