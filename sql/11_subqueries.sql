-- Scalar, IN, EXISTS, correlated subqueries
SELECT course_name, price
FROM courses
WHERE price > (SELECT AVG(price) FROM courses);

SELECT full_name
FROM users
WHERE user_id IN (SELECT user_id FROM projects WHERE deployed = 1);

SELECT u.full_name
FROM users u
WHERE EXISTS (
  SELECT 1 FROM enrollments e
  WHERE e.user_id = u.user_id AND e.status = 'dropped'
);

SELECT e.*
FROM enrollments e
WHERE e.score > (
  SELECT AVG(e2.score) FROM enrollments e2
  WHERE e2.course_id = e.course_id AND e2.score IS NOT NULL
);

-- PRACTICE:
-- 1. Find models with accuracy above the overall average non-null accuracy.
-- 2. Find users who have at least one completed course.
-- 3. Find projects with more stars than the average project.
