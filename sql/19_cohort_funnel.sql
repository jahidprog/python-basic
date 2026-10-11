-- Cohort analysis and simple learning funnel
WITH signup_cohorts AS (
  SELECT user_id, STRFTIME('%Y-%m', signup_date) AS cohort_month
  FROM users
),
first_enrollment AS (
  SELECT user_id, MIN(enrolled_at) AS first_enrolled_at
  FROM enrollments GROUP BY user_id
)
SELECT s.cohort_month, COUNT(*) AS signed_up,
       SUM(CASE WHEN f.user_id IS NOT NULL THEN 1 ELSE 0 END) AS enrolled,
       ROUND(1.0 * SUM(CASE WHEN f.user_id IS NOT NULL THEN 1 ELSE 0 END) / COUNT(*), 3) AS signup_to_enrollment_rate
FROM signup_cohorts s LEFT JOIN first_enrollment f ON f.user_id = s.user_id
GROUP BY s.cohort_month ORDER BY s.cohort_month;

SELECT
  COUNT(DISTINCT user_id) AS signed_up_users,
  COUNT(DISTINCT CASE WHEN status IN ('enrolled','in_progress','completed','dropped') THEN user_id END) AS enrolled_users,
  COUNT(DISTINCT CASE WHEN status = 'completed' THEN user_id END) AS users_with_completion
FROM enrollments;

-- PRACTICE:
-- 1. Calculate completion rate by signup cohort.
-- 2. Calculate drop rate per course.
-- 3. Compare signup-to-project and signup-to-deployment conversion rates.
