-- SQL feature engineering: turn raw tables into model-ready features
WITH enrollment_features AS (
  SELECT user_id,
    COUNT(*) AS enrollment_count,
    SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed_count,
    AVG(score) AS avg_score,
    SUM(amount_paid) AS total_spend
  FROM enrollments
  GROUP BY user_id
),
project_features AS (
  SELECT user_id,
    COUNT(*) AS project_count,
    SUM(CASE WHEN deployed = 1 THEN 1 ELSE 0 END) AS deployed_projects
  FROM projects
  GROUP BY user_id
),
user_features AS (
  SELECT u.user_id, u.country, u.signup_source,
    CAST(JULIANDAY('2025-08-01') - JULIANDAY(u.signup_date) AS INTEGER) AS account_age_days,
    COALESCE(e.enrollment_count, 0) AS enrollment_count,
    COALESCE(e.completed_count, 0) AS completed_count,
    e.avg_score,
    COALESCE(e.total_spend, 0) AS total_spend,
    COALESCE(p.project_count, 0) AS project_count,
    COALESCE(p.deployed_projects, 0) AS deployed_projects
  FROM users u
  LEFT JOIN enrollment_features e ON e.user_id = u.user_id
  LEFT JOIN project_features p ON p.user_id = u.user_id
)
SELECT * FROM user_features ORDER BY user_id;

-- PRACTICE:
-- 1. Build a user-level feature table with number of predictions, average confidence,
--    average latency, and observed prediction correctness rate.
-- 2. Create a course-level dataset with price, enrollment count, completion rate,
--    and average score.
-- NOTE: joining multiple one-to-many tables can multiply rows; aggregate each table
-- separately before joining when building production features.
