#!/usr/bin/node
const { dict } = require('./101-data');

// Create a new dictionary to store occurrences by user id
const occurrencesById = {};

// Iterate through the original dictionary to compute the new dictionary
for (const userId in dict) {
  const occurrences = dict[userId];

  // Check if the occurrences is a key in the new dictionary
  if (occurrences in occurrencesById) {
    occurrencesById[occurrences].push(userId);
  } else {
    occurrencesById[occurrences] = [userId];
  }
}

// Print the new dictionary
console.log(occurrencesById);
