CREATE DATABASE companydb;

USE companydb;

CREATE TABLE Employ
(
    Empno INT PRIMARY KEY,
    Name VARCHAR(30) NOT NULL,
    Gender ENUM('MALE','FEMALE'),
    Dept VARCHAR(30),
    Desig VARCHAR(30),
    Basic NUMERIC(9,2)
);

INSERT INTO Employ
(Empno, Name, Gender, Dept, Desig, Basic)
VALUES
(1, 'Sandhan', 'MALE', 'Java', 'Programmer', 88223),
(2, 'Premjeet', 'MALE', 'Sql', 'Expert', 98222),
(3, 'Nirmalya', 'MALE', 'Java', 'Developer', 88224),
(4, 'Zainab', 'FEMALE', 'Sql', 'Expert', 77224),
(5, 'Sourav', 'MALE', 'Dotnet', 'Manager', 77722),
(6, 'Ananta', 'MALE', 'Sql', 'Expert', 82555),
(7, 'Ishani', 'FEMALE', 'Dotnet', 'Expert', 77223);