#!/usr/bin/node
const args = process.argv;
const request = require('request');

request.get(args[2], function (error, response, body) {
  if (!error) {
    let count = 0;
    let id = 1;
    const userTask = {};
    const data = JSON.parse(body);
    for (const task of data) {
      if (task.userId === id) {
        // console.log(task.completed)
        if (task.completed === true) {
          count += 1;
        }
      } else if (task.completed === true && task.userId !== id) {
        id += 1;
        count = 1;
      }
      userTask[id] = count;
    }
    console.log(userTask);
  }
  // console.log(userTask);
});
