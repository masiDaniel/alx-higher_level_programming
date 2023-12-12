#!/usr/bin/node

function factorial (a) {
    if (isNaN(a) || a <= 1) {
      return 1;
    }
    return a * factorial(a - 1);
  }
  
  const args = process.argv.slice(2);
  
  console.log(factorial(parseInt(args[0])));