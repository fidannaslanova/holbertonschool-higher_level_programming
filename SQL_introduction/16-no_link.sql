-- Lists all records where name is not empty, ordered by score desc
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
