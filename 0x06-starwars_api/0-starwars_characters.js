#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the movie endpoint
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Recursive function to send requests to character URLs
function sendRequest(characterList, index) {
  // Base case: all characters have been processed
  if (characterList.length === index) {
    return;
  }

  // Send a request to the character URL
  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // Parse the response body as JSON and print the character name
      console.log(JSON.parse(body).name);

      // Recursively call the function for the next character
      sendRequest(characterList, index + 1);
    }
  });
}

// Send a request to the movie endpoint to get film details
request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Parse the response body as JSON and extract the character list
    const characterList = JSON.parse(body).characters;

    // Start sending requests to character URLs from index 0
    sendRequest(characterList, 0);
  }
});

