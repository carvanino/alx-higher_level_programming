#!/usr/bin/node

const args = process.argv;
const length = args.length;
switch (length) {
  case 2:
    console.log('No argument');
    break;
  case 3:
    console.log('Argument Found');
    break;
  default:
    console.log('Arguments Found');
    break;
}
