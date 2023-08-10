#!/usr/bin/node
/**
 * Script prints all characters of a Star Wars movie
 */

const request = require('request');

function getMovieCharacters(movieId) {
  const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching movie data:', error.message);
      return;
    }

    const movieData = JSON.parse(body);

    const charactersUrls = movieData.characters;
    const characterReq = charactersUrls.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (characterErr, characterResp, characterBody) => {
          if (characterErr) {
            reject(characterErr);
            return;
          }

          const characterData = JSON.parse(characterBody);
          resolve(characterData);
        });
      });
    });

    Promise.all(characterReq)
      .then((characters) => {
        characters.forEach((character) => {
          console.log(`${character.name}`);
        });
      })
      .catch((characterErr) => {
        console.error('Error fetching character data:', characterErr.message);
      });
  });
}

const args = process.argv.slice(2);
if (args.length !== 1) {
  // Display usage message if incorrect number of arguments
  console.log('Usage: node script.js <Movie ID>');
  process.exit(1);
}

const movieId = args[0];
getMovieCharacters(movieId);
