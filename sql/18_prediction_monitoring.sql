-- Prediction monitoring: latency, confidence, observed correctness
SELECT model_name, COUNT(*) AS requests,
       ROUND(AVG(latency_ms),2) AS avg_latency_ms,
       MAX(latency_ms) AS max_latency_ms,
       ROUND(AVG(confidence),3) AS avg_confidence,
       ROUND(AVG(was_correct),3) AS observed_accuracy
FROM predictions GROUP BY model_name;

SELECT model_name,
       SUM(CASE WHEN latency_ms > 300 THEN 1 ELSE 0 END) AS slow_requests,
       SUM(CASE WHEN confidence < 0.60 THEN 1 ELSE 0 END) AS low_confidence_requests,
       SUM(CASE WHEN was_correct = 0 THEN 1 ELSE 0 END) AS incorrect_predictions
FROM predictions GROUP BY model_name;

SELECT prediction_id, model_name, confidence, was_correct,
  CASE
    WHEN confidence >= 0.90 AND was_correct = 0 THEN 'High-confidence error'
    WHEN confidence < 0.60 THEN 'Low-confidence'
    ELSE 'Review normal'
  END AS review_bucket
FROM predictions;

-- PRACTICE:
-- 1. Calculate the 95th percentile latency (research SQLite-compatible approaches).
-- 2. Track daily request volume by model.
-- 3. Flag a model if observed accuracy is below 0.80 or average latency exceeds 300 ms.
