-- Window functions: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD
SELECT user_id, course_id, score,
  ROW_NUMBER() OVER (PARTITION BY course_id ORDER BY score DESC) AS row_num,
  RANK() OVER (PARTITION BY course_id ORDER BY score DESC) AS score_rank,
  DENSE_RANK() OVER (PARTITION BY course_id ORDER BY score DESC) AS dense_rank
FROM enrollments WHERE score IS NOT NULL;

SELECT prediction_id, model_name, requested_at, latency_ms,
  LAG(latency_ms) OVER (PARTITION BY model_name ORDER BY requested_at) AS previous_latency,
  latency_ms - LAG(latency_ms) OVER (PARTITION BY model_name ORDER BY requested_at) AS latency_change
FROM predictions;

SELECT user_id, enrolled_at, amount_paid,
  SUM(amount_paid) OVER (
    PARTITION BY user_id ORDER BY enrolled_at
    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
  ) AS cumulative_spend
FROM enrollments;

-- PRACTICE:
-- 1. Rank each user's courses by score.
-- 2. Return each model's most recent prediction using ROW_NUMBER.
-- 3. Calculate a running total of daily predictions.
