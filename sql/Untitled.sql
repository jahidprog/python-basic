CREATE DATABASE college;
USE college;

CREATE TABLE student(
    roll INT,
    name VARCHAR(50),
    age INT
);

INSERT INTO student
VALUES
(101,"Jahid", 26),
(102, "Bob", 25),
(103, "Charlie", 24);

SELECT * FROM student;

CREATE TABLE user(
    ID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Age INT,
    Email VARCHAR(100) UNIQUE,
    Followers INT DEFAULT 0,
    Following INT DEFAULT 0,
    CONSTRAINT age_check CHECK (age >= 13)
);

CREATE TABLE post(
    ID INT PRIMARY KEY, 
    Content VARCHAR(100),
    UserID INT,
    FOREIGN KEY (UserID) REFERENCES user(ID)
);

DROP TABLE user;