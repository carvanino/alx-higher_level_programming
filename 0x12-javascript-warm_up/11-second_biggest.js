#!/usr/bin/node

const args = process.argv;
const length = args.length;
let temp;

if (length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < length; i++) {
    for (let j = i + 1; j < length - 1; j++) {
      if (args[i] > args[j]) {
        temp = args[j];
        args[j] = args[i];
        args[i] = temp;
        /* console.log(args[i]); */
        /* console.log(args[j]); */
      }
    }
  }
  /* for (let i=2; i < length; i++) {
   * console.log(args[i]); */
  console.log(args[length - 2]);
}
/* console.log(args[length - 2]); */
/* console.log(args[3]); */
