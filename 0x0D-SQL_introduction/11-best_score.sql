-- This script lists all records with a score >= 10 from the table second_table, ordered by score
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
