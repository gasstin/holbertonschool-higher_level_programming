#!/usr/bin/node
/* task 4
Write a script that prints the number of movies
where the character “Wedge Antilles” is present.
*/
require('process');
const request = require('request');

const url = process.argv[2];
let counter = 0;

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // print error if occurs
  } else {
    const listOfMovies = JSON.parse(body).results;
    listOfMovies.forEach(element => {
      element.characters.forEach(element1 => {
        element1.split('/').forEach(element => {
          if (element === '18') {
            counter++;
          }
        });
      });
    });
    console.log(counter);
  }
});
