#!/usr/bin/node
const argvValues = process.argv;

if (argvValues.length >= 4) {
  console.log('Arguments found');
} else if (argvValues.length === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
