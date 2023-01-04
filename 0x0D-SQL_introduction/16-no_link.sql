-- lists records in database
-- DML query to show score and name
SELECT score, name FROM second_table
WHERE name != ''
ORDER BY score DESC;
