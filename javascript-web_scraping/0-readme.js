#!/usr/bin/node
/* task 0
Write a script that reads and prints the content of a file.
*/
require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
