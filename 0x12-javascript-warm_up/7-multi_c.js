#!/usr/bin/node

const { argv } = require('process');
const num = parseInt(argv[2]);
const clog = (cuantity) => {
  for (; cuantity > 0; cuantity--) console.log('C is fun');
};

Number.isInteger(num) ? clog(num) : console.log('Missing number of occurrences');
