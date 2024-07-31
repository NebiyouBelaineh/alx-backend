#!/usr/bin/env node

/**
 * job creator script using Kue
*/
import kue from 'kue';
const queue = kue.createQueue();

const jobData = {
    phoneNumber: '+251999999999',
    message: 'Good Morning',
}
const job = queue.create('push_notification_code', jobData).save((err) => {
    if (err) console.log(err.message);
    else console.log(`Notification job created: ${job.id}`);
});

job.on('job completed', () => {
    console.log('Notification job completed');
});
job.on('job failed', () => {
    console.log('Notification job failed');
});
