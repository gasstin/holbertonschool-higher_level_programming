#!/usr/bin/node
/* task 5
Write a script that gets the contents of a webpage
and stores it in a file.
*/
require('process');
const fs = require('fs');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // print error if occurs
  } else {
    fs.writeFileSync(process.argv[3], body, 'utf-8');
  }
});
