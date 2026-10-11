-- ML experiment analysis: compare model metrics and trade-offs
SELECT model_name, algorithm, dataset_name, accuracy, precision_score, recall_score, f1_score,
       train_minutes,
       ROUND(accuracy / NULLIF(train_minutes, 0), 4) AS accuracy_per_train_minute
FROM model_experiments
WHERE accuracy IS NOT NULL
ORDER BY f1_score DESC;

SELECT dataset_name, algorithm, accuracy, f1_score,
  RANK() OVER (PARTITION BY dataset_name ORDER BY f1_score DESC) AS rank_on_dataset
FROM model_experiments WHERE f1_score IS NOT NULL;

SELECT environment, COUNT(*) AS experiments,
       ROUND(AVG(train_minutes),2) AS avg_train_minutes,
       ROUND(AVG(accuracy),3) AS avg_accuracy
FROM model_experiments GROUP BY environment;

-- PRACTICE:
-- 1. Find the best F1 model for each dataset.
-- 2. Compare precision and recall gaps: ABS(precision_score - recall_score).
-- 3. Find experiments where accuracy is high (>0.9) but recall is below 0.85.
-- 4. Explain why accuracy alone may be misleading on imbalanced datasets.
