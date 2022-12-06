#!/usr/bin/node
/* task 7
    Write a function that returns the number of occurrences in a list:
*/

exports.nbOccurences = function (list, searchElement) {
  const listAuxiliar = list.filter((n) => n === searchElement);
  return listAuxiliar.length;
};
