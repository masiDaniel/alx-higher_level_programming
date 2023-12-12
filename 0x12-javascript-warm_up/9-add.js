#!/usr/bin/node

function add (a, b) {
    return a + b;
  }
  
  const args = process.argv.slice(2);
  const first = parseInt(args[0]);
  const second = parseInt(args[1]);
  
  console.log(add(first, second));