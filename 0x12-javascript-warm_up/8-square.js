#!/usr/bin/node
const myVar = process.argv[2];
const myNum = Number(myVar);
const myStr = 'X';
if (isNaN(myNum)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < myNum; index++) {
    console.log(myStr.repeat(myNum));
  }
}
