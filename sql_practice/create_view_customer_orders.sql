-- =====================================================================
-- File: create_view_customer_orders.sql
-- Purpose: Create a view named 'view1' combining customers and orders via inner join
-- =====================================================================

-- Drop the view if it already exists to prevent errors on re-run
DROP VIEW IF EXISTS view2;

-- Create the view using an INNER JOIN
CREATE VIEW view2 AS 
SELECT 
    c.customer_id, 
    c.customer_name, 
    o.order_id
FROM customers c
INNER JOIN orders o 
ON c.customer_id = o.customer_id;

-- Query the view to verify its contents
SELECT * FROM view2;