-- Advanced analytical patterns

-- 1) Top project per user (ties handled by RANK)
WITH ranked_projects AS (
  SELECT p.*,
    RANK() OVER (PARTITION BY user_id ORDER BY stars DESC) AS rnk
  FROM projects p
)
SELECT user_id, project_name, stars FROM ranked_projects WHERE rnk = 1;

-- 2) Moving average of prediction latency over each model's request stream
SELECT model_name, requested_at, latency_ms,
  AVG(latency_ms) OVER (
    PARTITION BY model_name ORDER BY requested_at
    ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
  ) AS moving_avg_latency
FROM predictions;

-- 3) Confusion-matrix-style counts when true outcome is represented by was_correct
SELECT model_name,
  SUM(CASE WHEN was_correct = 1 THEN 1 ELSE 0 END) AS correct_count,
  SUM(CASE WHEN was_correct = 0 THEN 1 ELSE 0 END) AS incorrect_count,
  COUNT(was_correct) AS labeled_count
FROM predictions GROUP BY model_name;

-- 4) Percent of total revenue per course
WITH revenue AS (
  SELECT course_id, SUM(amount_paid) AS course_revenue
  FROM enrollments GROUP BY course_id
)
SELECT c.course_name, r.course_revenue,
  ROUND(100.0 * r.course_revenue / NULLIF(SUM(r.course_revenue) OVER (), 0), 2) AS revenue_percent
FROM revenue r JOIN courses c ON c.course_id = r.course_id;

-- PRACTICE:
-- 1. Calculate each model's share of all prediction requests.
-- 2. Identify the 3 users with the most completed courses, including ties.
-- 3. Build a weekly monitoring report with request count, accuracy, and average latency.
