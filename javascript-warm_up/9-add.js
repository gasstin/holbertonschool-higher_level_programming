#!/usr/bin/node
/* task 9
    Write a script that prints the addition of 2 integers
*/
require('process');

function add (a, b) {
  console.log(a + b);
}

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
add(a, b);
