#!/usr/bin/node
/* task 8
    Write a function that returns the reversed version of a list
*/

exports.esrever = function (list) {
  let largo = 0;
  for (let index = 0; list[index]; index++) {
    largo++;
  }
  const reversedList = [];
  for (let index = 0; index < largo; index++) {
    reversedList[(largo - 1) - index] = list[index];
  }
  return reversedList;
};
