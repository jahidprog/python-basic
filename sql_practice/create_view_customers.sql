-- =====================================================================
-- File: create_view_customers.sql
-- Purpose: Create a view named 'view2' containing customer IDs
-- =====================================================================

-- Drop the view if it already exists to prevent errors on re-run
DROP VIEW IF EXISTS view1;

-- Create the view
CREATE VIEW view1 AS 
SELECT customer_id 
FROM customers;

-- Query the view to verify its contents
SELECT * FROM view1;