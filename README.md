Instructions:

1. Create database named gym by inputting the following into terminal - createdb gym
2. Link database to gym.sql - From root folder of gym_project: psql -d gym -f db/gym.sql. (Run this command twice)
3. Populate database using - python3 console.py
4. Start the flask server - flask run
5. Go to http://127.0.0.1:5000/ (Check *Running on xxx as this may be different)

Technologies used:

Python3, HTML, CSS, Flask, Jinja, PostgreSQL



BRIEF
Gym
A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP
The app should allow the gym to create and edit Members
The app should allow the gym to create and edit Classes
The app should allow the gym to book members on specific classes
The app should show a list of all upcoming classes
The app should show all members that are booked in for a particular class

Possible Extensions - NOT DONE YET
Classes could have a maximum capacity, and users can only be added while there is space remaining.
The gym could be able to give its members Premium or Standard membership. Standard members can only be signed up for classes during off-peak hours.
The Gym could mark members and classes as active/deactivated. Deactivated members/classes will not appear when creating bookings.


Screenshots:

