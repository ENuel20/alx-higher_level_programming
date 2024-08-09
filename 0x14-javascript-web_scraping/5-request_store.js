#!/usr/bin/node
const args = process.argv;
const req = require('request');
const fs = require('fs');

const url = args[2];
const fileName = args[3];

req.get(`${url}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(`${fileName}`, `${body}`, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
