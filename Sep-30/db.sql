CREATE DATABASE ml_demo;

USE ml_demo;

CREATE TABLE employee_salary
(
    id INT PRIMARY KEY AUTO_INCREMENT,
    experience DECIMAL(4,2),
    salary DECIMAL(10,2)
);



INSERT INTO employee_salary (experience, salary)
VALUES
(1, 30000),
(2, 35000),
(3, 40000),
(4, 45000),
(5, 50000),
(6, 55000),
(7, 60000),
(8, 65000),
(9, 70000),
(10, 75000);
