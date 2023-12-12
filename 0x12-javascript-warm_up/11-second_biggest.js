#!/usr/bin/node

function secondLargest (args) {
    const integers = args.map(arg => parseInt(arg));
  
    if (integers.length <= 1) {
      return 0;
    }
    integers.sort((a, b) => b - a);
  
    return integers[1];
  }
  
  const list = process.argv.slice(2);
  const result = secondLargest(list);
  
  console.log(result);