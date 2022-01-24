<h1>Gym Management System</h1>

First full stack solo project using Python3 with Flask, PostgreSQL, Psycopg2, HTML5, Jinja2 and CSS.

## The Brief

A local gym has asked you to build a piece of software to help them to manage memberships, and register members for classes.

MVP

- The app should allow the gym to create, edit and delete members 🟢
- The app should allow the gym to create, edit and delete classes 🟢
- The app should allow the gym to create and delete bookings 🟢
- The app should allow classes and members to be marked toggled as active/inactive with this reflecting correctly when creating a new booking 🟢

Extensions

- The app should allow classes to have a maximum capacity 🟡
- The app should show a list of all upcoming classes 🟡
- The app should show all members that are booked in for a particular class 🟡
- The app should show all classes a member is booked in for 🟡
- The app should allow for different membership types which determine the time the member can book classes 🟡


## Screenshots








## Instructions:

1. Create database named gym by inputting the following into terminal - createdb gym
2. Link database to gym.sql - From root folder of gym_project: psql -d gym -f db/gym.sql. (Run this command twice)
3. Populate database using - python3 console.py
4. Start the flask server - flask run
5. Go to http://127.0.0.1:5000/ (Check *Running on xxx as this may be different)





