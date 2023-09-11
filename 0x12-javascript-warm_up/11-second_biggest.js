#!/usr/bin/node
const myArgs = process.argv.slice(2).map(argv => Number(argv));
myArgs.sort();
myArgs.reverse();
if (isNaN(myArgs[1])) {
  console.log(0);
} else {
  console.log(myArgs[1]);
}
