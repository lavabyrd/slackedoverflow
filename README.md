# SlackedOverflow

## Overview
This is a WIP for a college project

## Technical Overview
When a slash command is run, the app will query all the users in that channel and send out a rolling direct message from the App bot to them asking them to provide thoughts about those users. Its can then give the users a way of asking for feedback on another user. e.g. 

> Hey John, please provide your thoughts on Anna in a thread reply!

Once the threaded reply is recieved for all users, it will send the full consolidated list to Anna with what her channel mates think.

## Technical methods and technology used
This app is written in Python 3.6 and uses the Slackclient SDK to ensure ease of calling the api methods required.

For more imformatio1n please see https://api.slack.com