#!/usr/bin/node
exports.logMe = function (item) {
  item.forEach((value, index) => {
    console.log(`${index}: ${value}`);
  });
};
