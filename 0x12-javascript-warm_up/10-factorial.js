#!/usr/bin/node

const argv = process.argv;
const num = Number(argv[2]);

console.log(factorial(num));

function factorial (num) {
  const cache = [];
  return ((() => {
    if (num === 1 || isNaN(num)) {
      return (1);
    }
    if (cache[num] !== undefined) {
      return (cache[num]);
    }
    cache[num] = num * factorial(num - 1);
    return (cache[num]);
  })());
}
