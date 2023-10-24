#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, async function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const chars = JSON.parse(body).characters;
    for (const char of chars) {
      await new Promise((resolve, reject) => {
        request(char, function (err, res, body) {
          if (err) {
            reject(err);
          }
          console.log(JSON.parse(body).name);
          resolve();
        });
      });
    }
  }
});
