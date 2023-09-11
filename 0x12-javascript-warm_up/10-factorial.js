#!/usr/bin/node
const myArg = process.argv[2];
const myNum = Number(myArg);
console.log(factorial(myNum));
function factorial (num) {
  if (isNaN(num) || (num <= 1)) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
