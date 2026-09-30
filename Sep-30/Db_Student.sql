CREATE DATABASE StudentDB;

USE StudentDB;

CREATE TABLE StudentPerformance
(
    StudyHours INT,
    Attendance INT,
    Marks INT
);

INSERT INTO StudentPerformance (StudyHours, Attendance, Marks)
VALUES
(2, 60, 45),
(4, 70, 55),
(6, 80, 68),
(8, 90, 82),
(10, 95, 92);

SELECT * FROM StudentPerformance;