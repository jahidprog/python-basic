-- INNER JOIN: Retrieves customers who have placed at least one order, 
-- and orders that belong to a valid customer.
SELECT 
    c.customer_id,
    c.customer_name,
    c.city,
    o.order_id,
    o.order_date,
    o.amount
FROM customers c
INNER JOIN orders o 
ON c.customer_id = o.customer_id;