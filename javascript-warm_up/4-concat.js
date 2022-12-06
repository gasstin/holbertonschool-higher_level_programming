#!/usr/bin/node
/* task 4
    Write a script that prints two arguments passed to it, in the following format: “ is ”
*/
import { argv } from 'node:process';

console.log('%s is %s', argv[2], argv[3]);
