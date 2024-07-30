#!/usr/bin/node
// Read from file using async/await

const fs = require('fs').promises;

const readFile = async (filePath) => {
  try {
    const data = await fs.readFile(filePath, 'utf-8');
    console.log(data);
  } catch (err) {
    console.error(err);
  }
};

readFile(process.argv[2]);
