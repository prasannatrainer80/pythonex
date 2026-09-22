DROP DATABASE IF EXISTS studentdb;

CREATE DATABASE studentdb;

USE studentdb;


-- =====================================================
-- STUDENT TABLE
-- =====================================================

CREATE TABLE Student
(
    StudentId INT PRIMARY KEY AUTO_INCREMENT,

    StudentName VARCHAR(50) NOT NULL,

    Gender VARCHAR(10),

    Course VARCHAR(50),

    Year INT,

    Email VARCHAR(100),

    Phone VARCHAR(15)
);


-- =====================================================
-- ATTENDANCE TABLE
-- =====================================================

CREATE TABLE Attendance
(
    AttendanceId INT PRIMARY KEY AUTO_INCREMENT,

    StudentId INT,

    MonthName VARCHAR(20),

    TotalDays INT,

    PresentDays INT,

    FOREIGN KEY(StudentId)
        REFERENCES Student(StudentId)
);


-- =====================================================
-- FEE PAYMENT TABLE
-- =====================================================

CREATE TABLE FeePayment
(
    PaymentId INT PRIMARY KEY AUTO_INCREMENT,

    StudentId INT,

    TotalFee DECIMAL(10,2),

    PaidAmount DECIMAL(10,2),

    PaymentDate DATE,

    FOREIGN KEY(StudentId)
        REFERENCES Student(StudentId)
);


-- =====================================================
-- MARKS TABLE
-- =====================================================

CREATE TABLE Marks
(
    MarkId INT PRIMARY KEY AUTO_INCREMENT,

    StudentId INT,

    Subject VARCHAR(50),

    InternalMarks INT,

    ExternalMarks INT,

    FOREIGN KEY(StudentId)
        REFERENCES Student(StudentId)
);
Insert student data
USE studentdb;

INSERT INTO Student
(
    StudentName,
    Gender,
    Course,
    Year,
    Email,
    Phone
)
VALUES
(
    'Ravi',
    'Male',
    'Python',
    1,
    'ravi@gmail.com',
    '9876543210'
),
(
    'Priya',
    'Female',
    'Python',
    1,
    'priya@gmail.com',
    '9876543211'
),
(
    'Kiran',
    'Male',
    'Data Science',
    2,
    'kiran@gmail.com',
    '9876543212'
),
(
    'Anitha',
    'Female',
    'Data Science',
    2,
    'anitha@gmail.com',
    '9876543213'
);



INSERT INTO Attendance
(
    StudentId,
    MonthName,
    TotalDays,
    PresentDays
)
VALUES

(1, 'June', 25, 23),
(1, 'July', 26, 24),
(1, 'August', 25, 22),

(2, 'June', 25, 20),
(2, 'July', 26, 23),
(2, 'August', 25, 24),

(3, 'June', 25, 21),
(3, 'July', 26, 22),
(3, 'August', 25, 23),

(4, 'June', 25, 24),
(4, 'July', 26, 25),
(4, 'August', 25, 24);

INSERT INTO FeePayment
(
    StudentId,
    TotalFee,
    PaidAmount,
    PaymentDate
)
VALUES

(1, 50000, 20000, '2026-06-10'),
(1, 50000, 15000, '2026-07-10'),

(2, 50000, 25000, '2026-06-15'),

(3, 60000, 30000, '2026-06-20'),

(4, 60000, 60000, '2026-06-25');


INSERT INTO Marks
(
    StudentId,
    Subject,
    InternalMarks,
    ExternalMarks
)
VALUES

(1, 'Python', 25, 65),
(1, 'SQL', 24, 68),
(1, 'Statistics', 22, 60),
(1, 'Data Analysis', 23, 70),

(2, 'Python', 24, 70),
(2, 'SQL', 25, 72),
(2, 'Statistics', 23, 65),
(2, 'Data Analysis', 24, 68),

(3, 'Python', 22, 62),
(3, 'SQL', 24, 70),
(3, 'Statistics', 20, 58),
(3, 'Data Analysis', 23, 65),

(4, 'Python', 26, 72),
(4, 'SQL', 25, 75),
(4, 'Statistics', 24, 70),
(4, 'Data Analysis', 26, 74);