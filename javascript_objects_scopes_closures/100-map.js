#!/usr/bin/node
/* task 11
    Write a script that imports an array and computes a new array.
*/

const ImportedList = require('./100-data').list;
const MapList = ImportedList.map((element, index) => element * index);
console.log(ImportedList);
console.log(MapList);
