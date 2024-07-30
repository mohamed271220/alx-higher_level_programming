#!/usr/bin/node
// Write to file using async/await

const fs = require('fs').promises;

const writeFile = async (filePath, content) => {
  try {
    await fs.writeFile(filePath, content, 'utf-8');
  } catch (err) {
    console.error(err);
  }
};

writeFile(process.argv[2], process.argv[3]);
