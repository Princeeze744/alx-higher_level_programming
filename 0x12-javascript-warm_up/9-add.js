#!/usr/bin/node

const argv = process.argv;
const a = Number(argv[2]);
const b = Number(argv[3]);

if (isNaN(a) || isNaN(b)) {
  console.log(NaN);
} else {
  add(a, b);
}

function add (a, b) {
  console.log(a + b);
}
