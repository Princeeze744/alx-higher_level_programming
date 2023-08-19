-- Script lists the number of records with same score in the table second_table of the database
-- list the nnumber of records with same score
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
