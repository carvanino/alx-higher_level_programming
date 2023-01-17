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
      if (task.userId === id && task.completed === true) {
	console.log("yes");
        count += 1;
      }
      else {

      userTask[id] = count;
      id += 1;
    }
    //console.log(userTask);
  }
  // console.log(userTask);
});
