#!/usr/bin/node
// This program displays the status code of a get request
const request = require('request');
request.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
