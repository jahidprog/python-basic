-- Create Customers table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    city VARCHAR(50)
);

-- Create Orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10, 2)
);

-- Insert sample data into Customers
INSERT INTO customers (customer_id, customer_name, city) VALUES
(1, 'Alice Smith', 'New York'),
(2, 'Bob Jones', 'Los Angeles'),
(3, 'Charlie Brown', 'Chicago'),
(4, 'Diana Prince', 'Houston');

-- Insert sample data into Orders
-- Note: customer_id 99 does not exist in customers (to test outer joins)
INSERT INTO orders (order_id, customer_id, order_date, amount) VALUES
(101, 1, '2026-01-10', 250.00),
(102, 1, '2026-01-15', 125.50),
(103, 2, '2026-01-18', 300.00),
(104, NULL, '2026-01-20', 45.00), -- Order with no customer assigned
(105, 99, '2026-01-22', 500.00); -- Order with orphaned customer_id