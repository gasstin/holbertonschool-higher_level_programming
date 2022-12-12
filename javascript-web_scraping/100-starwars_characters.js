#!/usr/bin/node
/* task 7
Write a script that prints all characters of a Star Wars movie:
*/
require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // print error if occurs
  } else {
    JSON.parse(body).characters.forEach(element => {
      request(element, function (error, response, body) {
        if (error) {
          console.error(error); // print error if occurs
        } else {
          console.log(JSON.parse(body).name);
        }
      }
      );
    });
  }
});
