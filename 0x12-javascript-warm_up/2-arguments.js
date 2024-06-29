#!/usr/bin/node
const arglen = process.argv.length - 2;
if (arglen < 1) {
  console.log('No argument');
} else if (arglen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
