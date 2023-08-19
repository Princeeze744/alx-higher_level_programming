-- Script select the names with the best score
-- query lists all records with score >= 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
