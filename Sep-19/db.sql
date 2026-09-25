DROP DATABASE IF EXISTS company_db;

CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employees
(
    empno INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    gender ENUM('MALE','FEMALE'),
    dept VARCHAR(30),
    desig VARCHAR(50),
    basic DECIMAL(10,2)
);

INSERT INTO employees
(empno,name,gender,dept,desig,basic)
VALUES
(1,'Sandhan','MALE','Java','Programmer',88223),
(2,'Premjeet','MALE','SQL','Developer',75000),
(3,'Anitha','FEMALE','Python','Data Analyst',92000),
(4,'Ravi','MALE','Python','Developer',85000),
(5,'Priya','FEMALE','Java','Programmer',78000),
(6,'Kavya','FEMALE','SQL','Data Analyst',95000),
(7,'Arun','MALE','Python','Senior Developer',120000),
(8,'Sita','FEMALE','Java','Senior Developer',115000),
(9,'Rahul','MALE','SQL','Developer',82000),
(10,'Meena','FEMALE','Python','Data Analyst',98000);
