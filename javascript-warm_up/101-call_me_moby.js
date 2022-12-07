#!/usr/bin/node
/* task 15
    Write a function that executes x times a function.
*/

exports.callMeMoby = function (x, theFunction) {
  for (let index = 0; index < x; index++) {
    theFunction();
  }
};
