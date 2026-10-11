-- Transactions and views (SQLite)
BEGIN TRANSACTION;
UPDATE courses SET price = price * 0.90 WHERE category = 'Data';
SELECT course_name, price FROM courses WHERE category = 'Data';
ROLLBACK; -- undo the demonstration update

-- Create a reusable view for model monitoring
DROP VIEW IF EXISTS model_monitoring_summary;
CREATE VIEW model_monitoring_summary AS
SELECT model_name, COUNT(*) AS request_count,
       ROUND(AVG(latency_ms), 2) AS avg_latency_ms,
       ROUND(AVG(was_correct), 3) AS observed_accuracy
FROM predictions
GROUP BY model_name;

SELECT * FROM model_monitoring_summary ORDER BY request_count DESC;

-- PRACTICE:
-- 1. Create a view showing completed enrollments with user and course names.
-- 2. Use a transaction to change a course price and roll it back.
