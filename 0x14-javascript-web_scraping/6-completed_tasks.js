#!/usr/bin/node
const url = process.argv[2];
const req = require('request');

req.get(`${url}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const done = {};
    const item = JSON.parse(body);
    for (let i = 0; i < item.length; i++) {
      const key = item[i].userId;
      if (item[i].completed) {
        if (done[key]) {
          done[key]++;
        } else {
          done[key] = 1;
        }
      }
    }
    console.log(done);
  }
});
