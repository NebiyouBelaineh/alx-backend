#!/usr/bin/env node

import kue from 'kue';
const queue = kue.createQueue();

const blackListedNums = ['4153518781', '4153518780'];

function sendNotification(phoneNumber, message, job, done) {
    // track progress from 0 to 100
    job.progress(0, 100);
    if (blackListedNums.includes(phoneNumber)) {
        job.failed();
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    else {
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
        job.progress(50, 100)
        done();
    }
}
queue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
})
