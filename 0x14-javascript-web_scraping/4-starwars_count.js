#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const count = body.split('/people/18').length - 1;
    console.log(count);
  }
});
