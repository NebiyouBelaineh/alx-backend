#!/usr/bin/env node
/**
 * redis client connection script
 */
// const redis = require('redis');
import redis from 'redis';
const client = redis.createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});
