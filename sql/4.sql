CREATE TABLE Teacher2(
    id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    subject VARCHAR(30),
    salary INT DEFAULT 25000
);

INSERT INTO Teacher2(id, name, subject, salary)
VALUES
(23, 'ajay', 'math', 50000),
(47, 'bharat', 'english', 60000),
(18, 'chetan', 'chemistry', 45000),
(9, 'diviya', 'physics', 75000);

SELECT * FROM teacher2;

-- select teacher whose salary is more than 55k
SELECT *
FROM teacher2
WHERE salary > 55000;

-- rename the salary column of teacher2 to ctc
ALTER TABLE teacher2
CHANGE COLUMN salary ctc INT;

-- update the salary of all teacher by giving them 25% increment
UPDATE teacher2
SET ctc = ctc + (ctc * 0.25);

-- add new column city with default "CTG"
ALTER TABLE teacher2
ADD COLUMN city VARCHAR(30) DEFAULT "CTG";

-- DELETE salary column
ALTER TABLE teacher2
DROP COLUMN ctc; 








