use crt;

drop table if exists login;

create table login
(
   username varchar(30) primary key,
   password varchar(30) NOT NULL
);

insert into login values('Himanshi','Kolage'),
('Samson','Peter'),('Raj','Kishore'),
('Mohan','Vamsi');
