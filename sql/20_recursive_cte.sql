-- Recursive CTE example: generate a sequence of numbers 1 through 12
WITH RECURSIVE months(n) AS (
  SELECT 1
  UNION ALL
  SELECT n + 1 FROM months WHERE n < 12
)
SELECT n FROM months;

-- Generate a date calendar for July 2025
WITH RECURSIVE calendar(day) AS (
  SELECT DATE('2025-07-01')
  UNION ALL
  SELECT DATE(day, '+1 day') FROM calendar WHERE day < '2025-07-31'
)
SELECT day FROM calendar;

-- PRACTICE:
-- 1. Generate dates for all of August 2025.
-- 2. Use a recursive CTE to generate numbers from 1 to 100.
