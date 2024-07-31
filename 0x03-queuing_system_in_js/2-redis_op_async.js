#!/usr/bin/env node
/**
 * redis client connection script
 */
// const redis = require('redis');
import redis from 'redis';
const client = redis.createClient();
const { promisify } = require('util');
const getAsync = promisify(client.get).bind(client);

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName)
    console.log(value);
    // console.log(value);
  }
  catch (err) {
    console.log(err.message);
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
