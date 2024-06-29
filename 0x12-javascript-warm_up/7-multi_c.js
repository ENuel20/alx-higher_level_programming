#!/usr/bin/node
const myVar1 = 'C is fun';
const x = parseInt(process.argv[2]);
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log(myVar1);
  }
} else {
  console.log('Missing number of occurrences');
}
