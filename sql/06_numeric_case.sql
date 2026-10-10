-- Arithmetic, ROUND, CASE expressions
SELECT course_name, price, ROUND(price * 1.10, 2) AS price_with_tax FROM courses;
SELECT model_name, accuracy, ROUND(accuracy * 100, 1) AS accuracy_percent
FROM model_experiments WHERE accuracy IS NOT NULL;

SELECT enrollment_id, score,
  CASE
    WHEN score >= 90 THEN 'A'
    WHEN score >= 80 THEN 'B'
    WHEN score >= 70 THEN 'C'
    WHEN score IS NULL THEN 'Not graded'
    ELSE 'Needs improvement'
  END AS score_band
FROM enrollments;

SELECT project_name,
  CASE WHEN deployed = 1 THEN 'Deployed' ELSE 'Not deployed' END AS deployment_status
FROM projects;

-- PRACTICE:
-- 1. Label predictions as high confidence (>=0.9), medium (0.7–0.899), or low.
-- 2. Give each course a price tier: free, budget (<25), standard (<60), premium.
