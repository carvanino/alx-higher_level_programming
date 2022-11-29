#!/usr/bin/node

const args = process.argv;
const length = args.length;
let temp;

if (length <= 3) {
  console.log(0);
} else {
  for (let i = 2; args[i]; i++) {
    for (let j = i + 1; args[j]; j++) {
      if (args[j] >= args[i]) {
        temp = args[j];
        args[j] = args[i];
        args[i] = temp;
        /* console.log(args[i]); */
        /* console.log(args[j]); */
      }
    }
	  /*console.log('i is:', i);*/
  }
  /*for (let i = 2; i < length; i++) {
    console.log(args[i]);
  }*/
  console.log(args[length - 2]);
}
