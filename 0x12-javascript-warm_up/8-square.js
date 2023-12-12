#!/usr/bin/node

const args = process.argv.slice(2);
const size = args[0];

if (Number.isInteger(parseInt(size))) {
  for (let i = 1; i <= size; i++) {
    let row = '';
    for (let j = 1; j <= size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}