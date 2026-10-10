-- WHERE, comparison operators, AND/OR/NOT, IN, BETWEEN, LIKE
SELECT * FROM courses WHERE price > 40;
SELECT * FROM users WHERE country = 'Bangladesh';
SELECT * FROM enrollments WHERE score BETWEEN 70 AND 90;
SELECT * FROM courses WHERE category IN ('Data','Machine Learning');
SELECT * FROM users WHERE signup_source <> 'organic';
SELECT * FROM projects WHERE project_name LIKE '%Assistant%';
SELECT * FROM users WHERE age IS NULL;
SELECT * FROM users WHERE country = 'Bangladesh' AND age >= 25;
SELECT * FROM courses WHERE price < 20 OR difficulty = 'Advanced';

-- PRACTICE:
-- 1. Find advanced courses priced below 80.
-- 2. Find users from Bangladesh or India who signed up after 2025-03-01.
-- 3. Find projects whose tech_stack mentions PyTorch.
