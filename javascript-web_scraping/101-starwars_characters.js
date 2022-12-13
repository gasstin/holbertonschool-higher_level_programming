#!/usr/bin/node
/* task 8
Write a script that prints all characters of a Star Wars movie in right order:
*/
require('process');
const request = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';

for (let index = 1; index <= 9; index++) {
  const urlToRequest = 'https://swapi-api.alx-tools.com/api/people/?page=' + index;
  request(urlToRequest, function (error, response, body) {
    if (error) {
      console.error(error); // print error if occurs
    } else {
      const actors = JSON.parse(body).results;
      actors.forEach(element => {
        if (element.films.includes(url)) {
          console.log(element.name);
        }
      });
    }
  });
}
