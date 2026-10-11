-- SQLite date/time functions
SELECT DATE('now') AS today;
SELECT signup_date, STRFTIME('%Y', signup_date) AS signup_year,
       STRFTIME('%m', signup_date) AS signup_month
FROM users;

SELECT DATE(completed_at) AS completion_day, COUNT(*) AS completions
FROM enrollments WHERE completed_at IS NOT NULL
GROUP BY DATE(completed_at) ORDER BY completion_day;

SELECT enrollment_id, enrolled_at, completed_at,
  CAST(JULIANDAY(completed_at) - JULIANDAY(enrolled_at) AS INTEGER) AS days_to_complete
FROM enrollments WHERE completed_at IS NOT NULL;

SELECT STRFTIME('%Y-%m', requested_at) AS month, COUNT(*) AS prediction_count
FROM predictions GROUP BY month ORDER BY month;

-- PRACTICE:
-- 1. Count signups by month.
-- 2. Find average days to course completion by course.
-- 3. List tickets unresolved for more than 24 hours (use a fixed reference date if desired).
