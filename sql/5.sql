-- Transaction ACID Property
SELECT @@autocommit;

-- Disable Autocommit 
SET autocommit = 0;
-- Enable Autocommit
SET autocommit = 1;


CREATE DATABASE prime;
USE prime;

CREATE TABLE account(
    ID INT PRIMARY KEY,
    Name VARCHAR(30),
    Balance DECIMAL(10, 2) 
);

ALTER TABLE account
MODIFY ID INT NOT NULL AUTO_INCREMENT;

INSERT INTO account(Name, Balance)
VALUES
('Adam', 500.00),
('Bob', 300.00),
('Charlie', 1000.00);

SELECT * FROM account;



