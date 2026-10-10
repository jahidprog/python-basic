-- INNER JOIN, LEFT JOIN, joining multiple tables
SELECT u.full_name, e.enrolled_at, c.course_name, e.status
FROM enrollments e
JOIN users u ON u.user_id = e.user_id
JOIN courses c ON c.course_id = e.course_id
ORDER BY u.full_name;

SELECT c.course_name, COUNT(e.enrollment_id) AS enrollment_count
FROM courses c LEFT JOIN enrollments e ON e.course_id = c.course_id
GROUP BY c.course_id, c.course_name
ORDER BY enrollment_count DESC;

SELECT u.full_name, p.project_name, p.domain
FROM users u LEFT JOIN projects p ON p.user_id = u.user_id
ORDER BY u.user_id;

-- PRACTICE:
-- 1. List every user and their projects, including users with no project.
-- 2. Show course name, enrolled user name, score, and status.
-- 3. Find users who have never enrolled in a course.
