CREATE TABLE house_price
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    area INT,
    bedrooms INT,
    age INT,
    price DECIMAL(12,2)
);

-- Insert data:

INSERT INTO house_price
(area, bedrooms, age, price)
VALUES
(1000, 2, 10, 5000000),
(1200, 2, 8, 6000000),
(1500, 3, 7, 7500000),
(1800, 3, 6, 9000000),
(2000, 4, 5, 10500000),
(2200, 4, 4, 12000000),
(2500, 4, 3, 14000000),
(2800, 5, 2, 16000000),
(3000, 5, 1, 18000000),
(3200, 5, 1, 19500000);