-- HAVING filters groups after aggregation
SELECT course_id, COUNT(*) AS enrollment_count
FROM enrollments GROUP BY course_id HAVING COUNT(*) >= 3;

SELECT user_id, SUM(amount_paid) AS lifetime_spend
FROM enrollments GROUP BY user_id HAVING SUM(amount_paid) > 50;

SELECT domain, COUNT(*) AS project_count
FROM projects GROUP BY domain HAVING COUNT(*) >= 2;

-- PRACTICE:
-- 1. Find countries with at least 3 users.
-- 2. Find courses whose average non-null score is above 80.
-- 3. Find models with at least 3 prediction records.
