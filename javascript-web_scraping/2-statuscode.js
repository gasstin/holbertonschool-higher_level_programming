#!/usr/bin/node
/* task 2
Write a script that display the status code of a GET request.
*/
require('process');
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error); // print error if occurs
  }
  console.log('code:', response.statusCode);
});
