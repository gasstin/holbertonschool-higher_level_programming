#!/usr/bin/node
/* task 3
Write a script that prints the title of a Star Wars
movie where the episode number matches a given integer.
*/
require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // print error if occurs
  } else {
    console.log(JSON.parse(body).title);
  }
});
