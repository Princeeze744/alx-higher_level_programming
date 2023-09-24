#!/usr/bin/node

const argv = process.argv;
if (argv[2] === undefined || isNaN(argv[2])) {
  console.log('Missing number of occurrences');
  process.exit();
}

for (let i = 0; i < parseInt(argv[2]); i++) {
  console.log('C is fun');
}
