#!/usr/bin/env node
/**
 * redis client to save hashes
 */

import redis from 'redis';
const client = redis.createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.message);
});
client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const objs = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2
}
for (const [key, value] of Object.entries(objs)) {
    client.hset('HolbertonSchools', key, value, redis.print)
}

client.hgetall('HolbertonSchools', (err, value) => {
    console.log(value);
})
