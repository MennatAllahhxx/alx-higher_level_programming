#!/usr/bin/node
exports.esrever = function (list) {
  let reversedArray = [];
  for (let index = list.length - 1; index >= 0; index--) {
    reversedArray.push(list[index]);
  }
  return (reversedArray);
};
