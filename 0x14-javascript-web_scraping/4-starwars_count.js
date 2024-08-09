#!/usr/bin/node
const req = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/';
const item = 'https://swapi-api.alx-tools.com/api/people/18/';

req.get(`${url}`, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let j = 0;
    for (let i = 0; i < results.length; i++) {
      // console.log(results[i]);
      let characters = results[i].characters;
      // console.log(characters);
      if (characters.includes(`${item}`)) {
        j++;
      }
    }
    console.log(j);
  }
});
