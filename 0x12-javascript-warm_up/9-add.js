#!/usr/bin/node
const argva = process.argv[2];
const argvb = process.argv[3];
const a = Number(argva);
const b = Number(argvb);
const result = add(a, b);
function add (a, b) {
  return (a + b);
}
console.log(result);
