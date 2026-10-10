-- ORDER BY, LIMIT, OFFSET
SELECT course_name, price FROM courses ORDER BY price DESC;
SELECT full_name, signup_date FROM users ORDER BY signup_date ASC;
SELECT project_name, stars FROM projects ORDER BY stars DESC LIMIT 5;
SELECT * FROM predictions ORDER BY latency_ms DESC LIMIT 3;
SELECT * FROM courses ORDER BY price ASC LIMIT 3 OFFSET 2;

-- PRACTICE:
-- 1. Show the 5 highest scoring enrollments.
-- 2. Show the 3 most recently registered users.
-- 3. Return the 4 slowest predictions.
