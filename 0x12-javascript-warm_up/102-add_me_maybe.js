#!/usr/bin/node

const myFunction = function (number, theFunction) {
  number++;
  theFunction(number);
};
module.exports.addMeMaybe = myFunction;
