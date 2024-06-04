#!/usr/bin/node
// Print all the characters of a star wars movie

const request = require('request');
request.get('https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (error, response, body) {
    if (error) {
      console.log(error);
    }
    const data = JSON.parse(body);
    const characters = data.characters;
    for (const character of characters) {
      request.get(character, function (error, response, _body) {
        if (error) {
          console.log(error);
        }
        const _data = JSON.parse(_body);
        console.log(_data.name);
      });
    }
  });
