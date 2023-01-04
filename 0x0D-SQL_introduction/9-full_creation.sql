-- Create a new table
-- DDL query to create new table
CREATE TABLE IF NOT EXISTS second_table
(id INT,
 name VARCHAR(256),
 score INT);
-- DML query to insert first row
INSERT INTO second_table (id, name, score)
VALUES (1, 'John', 10);
-- DML query for second row
INSERT INTO second_table (id, name, score)
VALUES (2, 'Alex', 3);
--DML query thrid row
INSERT INTO second_table (id, name, score)
VALUES (3, 'Bob', 14);
--DML query fouth row
INSERT INTO second_table (id, name, score)
VALUES (4, 'George', 8);
