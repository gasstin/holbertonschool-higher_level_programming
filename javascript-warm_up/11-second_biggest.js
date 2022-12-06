#!/usr/bin/node
/* task 11
    Write a script that searches the second biggest integer
    in the list of arguments.
*/
require('process');

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const listOfArguments = [];
  for (let index = 2; index < process.argv.length; index++) {
    listOfArguments.push(parseInt(process.argv[index])); // create a list arguments
  }
  listOfArguments.sort((a, b) => b - a); // sort the list
  console.log(listOfArguments[1]);
}
