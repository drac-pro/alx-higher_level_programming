#!/usr/bin/node
const dict = require('./101-data').dict;
const dictByOccurance = (dict) => {
  const newDict = {};
  for (const [userId, occurance] of Object.entries(dict)) {
    if (!newDict[occurance]) {
      newDict[occurance] = [];
    }
    newDict[occurance].push(userId);
  }
  return newDict;
};

const newDict = dictByOccurance(dict);
console.log(newDict);
