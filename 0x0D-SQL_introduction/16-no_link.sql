-- Script lists all records of the table second_table
-- lists all records where name is not null
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
