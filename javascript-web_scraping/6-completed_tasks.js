#!/usr/bin/node
/* task 6
Write a script that computes the number of tasks
completed by user id.
*/
require('process');
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error); // print error if occurs
  } else {
    const data = JSON.parse(body);
    const finalDict = {};
    let index = 0;
    while (data[index]) {
      if (data[index].completed === true) {
        if (data[index].userId in finalDict) {
          finalDict[data[index].userId]++;
        } else {
          finalDict[data[index].userId] = 1;
        }
      }
      index++;
    }
    console.log(finalDict);
  }
});
