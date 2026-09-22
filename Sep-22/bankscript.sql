DROP DATABASE IF EXISTS banknew;

CREATE DATABASE banknew;

USE banknew;

CREATE TABLE Accounts
(
    AccountNo INT PRIMARY KEY,
    AccHolderName VARCHAR(30),
    UserName VARCHAR(30) UNIQUE,
    Passcode VARCHAR(30),
    Email VARCHAR(30) UNIQUE,
    MobileNo VARCHAR(20) UNIQUE,
    Amount NUMERIC(9,2)
);

CREATE TABLE Trans
(
    TranID INT PRIMARY KEY AUTO_INCREMENT,
    AccountNo INT,
    TranAmount NUMERIC(9,2),
    TranType VARCHAR(5),
    FOREIGN KEY (AccountNo) REFERENCES Accounts(AccountNo)
);

INSERT INTO Accounts
(AccountNo,AccHolderName, UserName, Passcode, Email, MobileNo, Amount)
VALUES
(1,'Geethika','Geethika12','Vuppala',
 'Geethika@gmail.com','9999888812',88234.22),

(2,'Nitisha','Nitisha1','Sagar',
 'Nitisha@gmail.com','8888999913',88222.22);