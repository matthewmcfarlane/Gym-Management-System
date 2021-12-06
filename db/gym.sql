DROP TABLE bookings;
DROP TABLE members;
DROP TABLE fitness_classes;



CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR (255),
    dob VARCHAR (255),
    email VARCHAR(255),
    membership_type VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE fitness_classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    capacity INT,
    start_time VARCHAR(255),
    duration INT,
    day VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    fitness_class_id INT REFERENCES fitness_classes(id) ON DELETE CASCADE
);
