-- SELECT, column selection, aliases, DISTINCT
SELECT * FROM users;
SELECT full_name, country FROM users;
SELECT full_name AS name, signup_date AS joined_on FROM users;
SELECT DISTINCT country FROM users;
SELECT DISTINCT signup_source FROM users;

-- PRACTICE:
-- 1. Show only course_name and price from courses.
-- 2. List unique project domains.
-- 3. Show each user's name and signup source with readable aliases.
