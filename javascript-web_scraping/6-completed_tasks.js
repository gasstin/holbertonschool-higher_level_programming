#!/usr/bin/node
/* task 6
Write a script that computes the number of tasks
completed by user id.
*/
require('process');
const request = require('request');

let url = '';
if (process.argv[2] === 'https://jsonplaceholder.typicode.com/todos') {
  url = process.argv[2] + '/?completed=true';
} else {
  url = process.argv[2];
}
const finalDict = {};
request(url, function (error, response, body) {
  if (error) {
    console.error(error); // print error if occurs
  } else {
    const data = JSON.parse(body);
    let index = 0;
    while (data[index]) {
      if (data[index].userId in finalDict) {
        finalDict[data[index].userId]++;
      } else {
        finalDict[data[index].userId] = 1;
      }
      index++;
    }
    console.log(finalDict);
  }
});
