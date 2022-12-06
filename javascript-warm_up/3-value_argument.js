#!/usr/bin/node
/* task 3 */
require('process')

if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log('No argument');
}
