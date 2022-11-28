#!/usr/bin/node

const args = process.argv;
const length = args.length;
let temp;

if (length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < length; i++) {
    for (let j = i + 1; j < length; j++) {
      if (args[j] > args[i]) {
        temp = args[j];
        args[j] = args[i];
        args[i] = temp;
      }
    }
  }
  console.log(args[3]);
}
/* console.log(args[3]); */
