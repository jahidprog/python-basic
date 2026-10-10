-- COUNT, SUM, AVG, MIN, MAX, GROUP BY
SELECT COUNT(*) AS total_users FROM users;
SELECT AVG(age) AS average_age FROM users;
SELECT country, COUNT(*) AS user_count FROM users GROUP BY country ORDER BY user_count DESC;
SELECT status, COUNT(*) AS enrollments FROM enrollments GROUP BY status;
SELECT course_id, ROUND(AVG(score),2) AS average_score
FROM enrollments WHERE score IS NOT NULL GROUP BY course_id;
SELECT SUM(amount_paid) AS revenue FROM enrollments;
SELECT domain, AVG(stars) AS average_stars, MAX(stars) AS top_stars
FROM projects GROUP BY domain;

-- PRACTICE:
-- 1. Count users by signup_source.
-- 2. Calculate revenue by course_id.
-- 3. Find the average latency and accuracy for each model_name in predictions.
