#!/usr/bin/env node

const fs = require('fs');
const process = require('process');
const file = process.argv[2]; // Correctly access the first argument passed to the script

fs.readFile(file, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data);
});

