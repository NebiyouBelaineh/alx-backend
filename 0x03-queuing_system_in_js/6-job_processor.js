#!/usr/bin/env node

import kue from 'kue';
const queue = kue.createQueue();

function sendNotifcation(phoneNumber, message) {
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

queue.process('push_notification_code', (job, done) => {
    sendNotifcation(job.data.phoneNumber, job.data.message);
    done();
});
