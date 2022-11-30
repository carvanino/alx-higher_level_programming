#!/usr/bin/node
const list = require('./100-data.js').list;
const rev = list.map((x, i) => x * i);

console.log(list);
console.log(rev);
