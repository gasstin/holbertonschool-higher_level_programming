#!/usr/bin/node
/* task 8
Write a script that prints all characters of a Star Wars movie in right order:
*/
require('process');
const request = require('request');

///////////////////

function request_actors (url, index) {
  const urlToCheck = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2] + '/';
  let actorsList = '';
  request(url, function (error, response, body) {
    if (error) {
      console.error(error); // print error if occurs
    } else {
      const actors = JSON.parse(body).results;
      actors.forEach(element => {
        if (element.films.includes(urlToCheck)) {
          actorsList += index + ',' + element.name + ',';
        }
      });
      } 
      actorsList = actorsList.split(',');
      for (let indexAux = 0; indexAux < actorsList.length; indexAux++) {
          if (actorsList[indexAux] == index) {
            console.log(actorsList[indexAux + 1]);
          }
      }
      })
  };

for (let index = 1; index <= 9; index++) {
const urlToRequest = 'https://swapi-api.alx-tools.com/api/people/?page=' + index;
  request_actors(urlToRequest, index);
}
  