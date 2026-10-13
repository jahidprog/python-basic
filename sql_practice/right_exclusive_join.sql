-- RIGHT EXCLUSIVE JOIN
SELECT 
    c.customer_id,
    c.customer_name,
    c.city
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id
WHERE c.customer_id IS NULL;