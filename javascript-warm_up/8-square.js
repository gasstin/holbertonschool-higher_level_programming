#!/usr/bin/node
/* task 8
    Write a script that prints a square
*/
require('process');

if (parseInt(process.argv[2])) {
  let toPrint = '';
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    toPrint += 'X';
  }
  for (let index = 0; index < parseInt(process.argv[2]); index++) {
    console.log(toPrint);
  }
} else {
  console.log('Missing size');
}
