-- UNION, UNION ALL, INTERSECT, EXCEPT
SELECT country AS location FROM users
UNION
SELECT environment AS location FROM model_experiments;

SELECT user_id FROM enrollments WHERE status = 'completed'
UNION
SELECT user_id FROM projects WHERE deployed = 1;

SELECT user_id FROM enrollments
INTERSECT
SELECT user_id FROM projects;

SELECT user_id FROM users
EXCEPT
SELECT user_id FROM enrollments;

-- PRACTICE:
-- 1. Combine course categories and project domains into one unique list.
-- 2. Find users with projects but no enrollments using EXCEPT.
