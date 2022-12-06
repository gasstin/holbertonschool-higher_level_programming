#!/usr/bin/node
/* task 7
    Write a script that prints x times “C is fun”
*/
import { argv } from 'node:process';

if (parseInt(argv[2])) {
  for (let index = 0; index < parseInt(argv[2]); index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
