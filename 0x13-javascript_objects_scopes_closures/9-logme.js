#!/usr/bin/node
exports.logMe = function (item) {
  static count = 0;
  console.log(count + ": " + item);
  count++;
};
