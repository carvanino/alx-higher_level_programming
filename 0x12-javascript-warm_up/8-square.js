#!/usr/bin/node

const args = process.argv;

let number = args[2];
let square = '';

if (isNaN(number)) {
  console.log('Missing size');
} else {
  for (let i = args[2]; i > 0; i--) {
    for (number; number > 0; number--) {
      square += 'X';
    }
    console.log(square);
  }
}
