#!/usr/bin/node
const myVar = process.argv[2];
const myNum = Number(myVar);
if (isNaN(myNum)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + myNum);
}
