#!/usr/bin/node
/* task 12
    Write a script that imports a dictionary of occurrences by user id
    and computes a dictionary of user ids by occurrence.
*/

const ImportedDict = require('./101-data').dict;
const KeysImported = Object.keys(ImportedDict);
const ValuesImported = Object.values(ImportedDict);
const newdict = {};
for (let index2 = 0; index2 < ValuesImported.length; index2++) {
  const ListOfOccur = [];
  for (let index1 = 0; index1 < KeysImported.length; index1++) {
    if (ImportedDict[KeysImported[index1]] === ValuesImported[index2]) {
      ListOfOccur.push(KeysImported[index1]); // append the list
    }
  }
  newdict[ValuesImported[index2]] = ListOfOccur; // add the key
}
console.log(newdict);
