-- SQL feature engineering: turn raw tables into model-ready features
WITH user_features AS (
  SELECT u.user_id, u.country, u.signup_source,
    CAST(JULIANDAY('2025-08-01') - JULIANDAY(u.signup_date) AS INTEGER) AS account_age_days,
    COUNT(e.enrollment_id) AS enrollment_count,
    SUM(CASE WHEN e.status = 'completed' THEN 1 ELSE 0 END) AS completed_count,
    AVG(e.score) AS avg_score,
    COALESCE(SUM(e.amount_paid), 0) AS total_spend,
    COUNT(p.project_id) AS project_count,
    SUM(CASE WHEN p.deployed = 1 THEN 1 ELSE 0 END) AS deployed_projects
  FROM users u
  LEFT JOIN enrollments e ON e.user_id = u.user_id
  LEFT JOIN projects p ON p.user_id = u.user_id
  GROUP BY u.user_id
)
SELECT * FROM user_features ORDER BY user_id;

-- PRACTICE:
-- 1. Build a user-level feature table with number of predictions, average confidence,
--    average latency, and observed prediction correctness rate.
-- 2. Create a course-level dataset with price, enrollment count, completion rate,
--    and average score.
-- NOTE: joining multiple one-to-many tables can multiply rows; aggregate each table
-- separately before joining when building production features.
