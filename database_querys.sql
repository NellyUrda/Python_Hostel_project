create database hotel;

CREATE TABLE rooms (RoomNr CHAR(3), RoomType VARCHAR(10),RoomPrice int(10));
ALTER TABLE rooms ADD PRIMARY KEY (RoomNr);

INSERT INTO rooms VALUES ('101','single','300');  
INSERT INTO rooms VALUES('102','double','400');
INSERT INTO rooms VALUES('103','double del','500');
INSERT INTO rooms VALUES('104','family','600');


CREATE TABLE clients (clientID char(10),clientName varchar(10),clientAdresse text(30),roomNr char(3), checkIn Date ,checkOut Date); 
ALTER TABLE clients ADD CONSTRAINT FOREIGN KEY (RoomNr) REFERENCES rooms (RoomNr);
