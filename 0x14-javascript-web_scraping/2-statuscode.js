#!/usr/bin/node

const sts = require('request');
sts.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
