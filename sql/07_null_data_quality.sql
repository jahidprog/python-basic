-- NULL handling, COALESCE, data quality checks
SELECT full_name, COALESCE(country, 'Unknown') AS country FROM users;
SELECT enrollment_id, COALESCE(score, 0) AS score_or_zero FROM enrollments;
SELECT COUNT(*) AS total_users, COUNT(age) AS users_with_age FROM users;
SELECT * FROM users WHERE email IS NULL OR TRIM(email) = '';
SELECT email, COUNT(*) AS copies FROM users GROUP BY email HAVING COUNT(*) > 1;
SELECT * FROM predictions WHERE confidence IS NULL OR latency_ms IS NULL;
SELECT * FROM model_experiments WHERE accuracy IS NULL;

-- PRACTICE:
-- 1. Count enrollments with missing scores.
-- 2. Find projects missing tech_stack or started_at.
-- 3. Check whether any model has F1 outside the 0–1 range.
