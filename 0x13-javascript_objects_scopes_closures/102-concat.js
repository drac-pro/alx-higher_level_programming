#!/usr/bin/node
const fs = require('fs');
const path = require('path');
if (process.argv.length >= 5) {
  const [,, firstFilePath, secondFilePath, destinationFilePath] = process.argv;
  const firstFileContent = fs.readFileSync(path.resolve(firstFilePath), { encoding: 'utf8' });
  const secondFileContent = fs.readFileSync(path.resolve(secondFilePath), { encoding: 'utf8' });
  const concatenatedContent = firstFileContent + secondFileContent;
  fs.writeFileSync(path.resolve(destinationFilePath), concatenatedContent);
}
