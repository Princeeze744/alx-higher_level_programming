-- Script creates a new table 'second_table' in the current database
-- query creates a new table in the current database
CREATE TABLE IF NOT EXISTS second_table(
	id INT,
	name VARCHAR(256),
	score INT);
-- inserts new record for John
INSERT INTO second_table
VALUES(1, "John", 10);
-- inserts new record for Alex
INSERT INTO second_table
VALUES(2, "Alex", 3);
-- inserts new record for Bob
INSERT INTO second_table
VALUES(3, "Bob", 14);
-- inserts new record for George
INSERT INTO second_table
VALUES(4, "George", 8);
