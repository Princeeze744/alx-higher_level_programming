#!/usr/bin/node

const argv = process.argv;
const size = parseInt(argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
  process.exit();
}

for (let i = 0; i < size; i++) {
  let str = '';
  for (let j = 0; j < size; j++) {
    str = str + 'X';
  }
  console.log(str);
}
