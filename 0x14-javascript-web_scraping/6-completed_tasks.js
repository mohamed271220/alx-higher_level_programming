#!/usr/bin/node
// web scrapper

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasksCompleted = {};
  body.forEach(todo => {
    if (todo.completed) {
      tasksCompleted[todo.userId] = tasksCompleted[todo.userId] ? tasksCompleted[todo.userId] + 1 : 1;
    }
  });
  console.log(tasksCompleted);
});
