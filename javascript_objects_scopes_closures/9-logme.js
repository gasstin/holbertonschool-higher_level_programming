#!/usr/bin/node
/* task 9
    Write a function that prints the number of arguments
    already printed and the new argument value
*/

let NumberOfArguments = 0;
exports.logMe = function (item) {
  console.log('%d: %s', NumberOfArguments, item);
  NumberOfArguments++;
};
