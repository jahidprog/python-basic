-- LEFT JOIN: Retrieves ALL customers, whether they have placed an order or not.
SELECT 
    c.customer_id,
    c.customer_name,
    c.city,
    o.order_id,
    o.order_date,
    o.amount
FROM 
    customers c
LEFT JOIN 
    orders o ON c.customer_id = o.customer_id;