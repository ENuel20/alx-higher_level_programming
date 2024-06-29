#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!isNaN(x)) {
  const str = 'X';
  const width = str.repeat(x);
  for (let j = 0; j < x; j++) {
    console.log(width);
  }
} else {
  console.log('Missing size');
}
