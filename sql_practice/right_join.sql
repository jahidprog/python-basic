-- RIGHT JOIN: Retrieves ALL orders, even if they don't match any customer.
SELECT 
    c.customer_id,
    c.customer_name,
    c.city,
    o.order_id,
    o.order_date,
    o.amount
FROM customers c
RIGHT JOIN orders o 
ON c.customer_id = o.customer_id;