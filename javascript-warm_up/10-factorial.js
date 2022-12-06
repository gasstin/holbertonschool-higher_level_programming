#!/usr/bin/node
/* task 10
    Write a script that computes and prints a factorial
*/
require('process');

function factorialTask (a) {
  let result;
  if ((a === null) | (a === 1)) {
    result = 1;
  } else {
    result = a * factorialTask(a - 1);
  }
  return result;
}

console.log(factorialTask(process.argv[2]));
