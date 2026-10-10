-- SQLite string functions: lower, upper, trim, length, substr, replace, instr
SELECT UPPER(full_name) AS uppercase_name FROM users;
SELECT LOWER(email) AS normalized_email FROM users;
SELECT TRIM('   SQL practice   ') AS cleaned_text;
SELECT full_name, LENGTH(full_name) AS name_length FROM users;
SELECT SUBSTR(email, INSTR(email, '@') + 1) AS email_domain FROM users;
SELECT REPLACE(tech_stack, 'Python', 'PYTHON') FROM projects;

-- PRACTICE:
-- 1. Display each country in uppercase.
-- 2. Extract the first 3 characters of each course name.
-- 3. Find projects where tech_stack contains 'SQL'.
