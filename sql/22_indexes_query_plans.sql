-- Indexes and query plans
-- Schema file already creates a few indexes. Inspect query plan:
EXPLAIN QUERY PLAN
SELECT * FROM predictions
WHERE model_name = 'churn-v3' AND requested_at >= '2025-07-01';

-- Example composite index for this filter pattern:
CREATE INDEX IF NOT EXISTS idx_predictions_model_date
ON predictions(model_name, requested_at);

-- Compare a search on an indexed column and a non-indexed expression:
EXPLAIN QUERY PLAN SELECT * FROM users WHERE signup_date = '2025-05-20';
EXPLAIN QUERY PLAN SELECT * FROM users WHERE DATE(signup_date) = '2025-05-20';

-- PRACTICE:
-- 1. Add an index for support_tickets(status, created_at).
-- 2. Explain why wrapping an indexed column in a function can reduce index use.
-- 3. Use EXPLAIN QUERY PLAN to inspect a join between enrollments and courses.
-- Tip: indexes speed up many reads but use storage and add overhead to writes.
