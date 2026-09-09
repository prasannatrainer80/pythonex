CREATE DATABASE sales_db;

USE sales_db;

CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    order_date DATE,
    product VARCHAR(100),
    category VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2)
);



INSERT INTO sales
(order_id, order_date, product, category, quantity, price)
VALUES
(1, '2026-01-05', 'Laptop', 'Electronics', 2, 800.00),
(2, '2026-01-10', 'Mouse', 'Electronics', 5, 25.00),
(3, '2026-01-15', 'Keyboard', 'Electronics', 3, 50.00),
(4, '2026-01-20', 'Chair', 'Furniture', 3, 150.00),
(5, '2026-02-03', 'Laptop', 'Electronics', 1, 800.00),
(6, '2026-02-08', 'Desk', 'Furniture', 2, 300.00),
(7, '2026-02-15', 'Mouse', 'Electronics', 10, 25.00),
(8, '2026-03-01', 'Laptop', 'Electronics', 3, 800.00),
(9, '2026-03-12', 'Chair', 'Furniture', 4, 150.00),
(10, '2026-03-20', 'Keyboard', 'Electronics', 5, 50.00);