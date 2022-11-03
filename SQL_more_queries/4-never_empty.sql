-- task 4
-- Write a script that creates the table id_not_null on your MySQL server.
CREATE TABLE IF NOT EXISTS force_name
    (id INT = 1, name VARCHAR(256) NOT NULL);