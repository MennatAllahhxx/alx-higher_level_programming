#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const usrsTasks = {};
    const tasks = JSON.parse(body);
    for (let idx = 0; idx < tasks.length; idx++) {
      const usrId = tasks[idx].userId;
      if (tasks[idx].completed) {
        if (usrId in usrsTasks) {
          usrsTasks[usrId] += 1;
        } else {
          usrsTasks[usrId] = 1;
        }
      }
    }
    console.log(usrsTasks);
  }
});
