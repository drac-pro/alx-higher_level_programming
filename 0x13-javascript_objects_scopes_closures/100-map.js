#!/usr/bin/node
const list = require('./100-data');
console.log(list);
const newList = list.map(function (value, index) {
  return value * index;
});
console.log(newList);
