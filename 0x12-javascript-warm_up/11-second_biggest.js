#!/usr/bin/node
const myArgs = process.argv.slice(2).map(Number).sort((a, b) => b - a);
if (isNaN(myArgs[1]) || myArgs[1] === undefined) {
  console.log(0);
} else {
  console.log(myArgs[1]);
}
