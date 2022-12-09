#!/usr/bin/node
/* task 13
    Write a script that imports a dictionary of occurrences by user id
    and computes a dictionary of user ids by occurrence.
*/
require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) throw err;
  fs.writeFile(process.argv[4], data, (err1) => {
    // In case of a error throw err
    if (err1) throw err;
  });
});
fs.readFile(process.argv[3], 'utf8', function (err, data) {
  if (err) throw err;
  fs.appendFile(process.argv[4], data, (err1) => {
    // In case of a error throw err
    if (err1) throw err;
  });
});
