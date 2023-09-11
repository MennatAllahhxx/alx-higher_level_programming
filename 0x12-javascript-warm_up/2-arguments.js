#!/usr/bin/node
if (process.argv.length === 1) {
  console.error('No argument');
} else if (process.argv.length === 2) {
  console.error('Argument found');
} else {
  console.error('Arguments found');
}
