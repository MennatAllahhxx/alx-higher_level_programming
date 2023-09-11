#!/usr/bin/node
const myVar = process.argv[2];
const myNum = Number(myVar);
if (isNaN(myNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < myNum; index++) {
    console.log('C is fun');
  }
}
