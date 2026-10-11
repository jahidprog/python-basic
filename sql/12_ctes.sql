-- Common Table Expressions (CTEs) improve readability
WITH course_stats AS (
  SELECT course_id, COUNT(*) AS enrollments,
         ROUND(AVG(score), 2) AS avg_score
  FROM enrollments GROUP BY course_id
)
SELECT c.course_name, s.enrollments, s.avg_score
FROM course_stats s JOIN courses c ON c.course_id = s.course_id
ORDER BY s.enrollments DESC;

WITH model_metrics AS (
  SELECT model_name, AVG(confidence) AS avg_confidence,
         AVG(latency_ms) AS avg_latency,
         AVG(was_correct) AS observed_accuracy
  FROM predictions GROUP BY model_name
)
SELECT model_name, ROUND(avg_confidence,3) AS avg_confidence,
       ROUND(avg_latency,1) AS avg_latency_ms,
       ROUND(observed_accuracy,3) AS observed_accuracy
FROM model_metrics;

-- PRACTICE:
-- 1. Use a CTE to calculate spending per user, then list users spending over 50.
-- 2. Use a CTE to calculate project count and deployed-project count per user.
