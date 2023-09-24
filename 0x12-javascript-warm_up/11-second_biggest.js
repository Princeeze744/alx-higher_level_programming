#!/usr/bin/node
const args = process.argv;
let max, secondMax;
max = secondMax = 0;

for (let i = 0; i < args.length; i++) {
  const temp = parseInt(args[i]);
  if (temp > max) {
    secondMax = max;
    max = temp;
  } else {
    if (temp > secondMax) {
      secondMax = temp;
    }
  }
}
console.log(secondMax);
