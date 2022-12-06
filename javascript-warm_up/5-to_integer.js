#!/usr/bin/node
/* task 5
    Write a script that prints My number: <first argument converted in integer>
    if the first argument can be converted to an integer:
*/
import { argv } from 'node:process';

if (parseInt(argv[2])) {
  console.log('My number: %d', parseInt(argv[2]));
} else {
  console.log('Not a number');
}
