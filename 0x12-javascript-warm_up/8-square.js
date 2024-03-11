#!/usr/bin/node
if (!isNaN(process.argv[2])) {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    let square = '';
    for (let j = 0; j < size; j++) {
      square += 'X';
    }
    console.log(square);
  }
} else {
  console.log('Missing size');
}
