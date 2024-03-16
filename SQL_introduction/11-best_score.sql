-- lists all record with a score >= 10 in second_table (db hbtn_0c_0)
SELECT score, name
from second_table
WHERE score >= 10
ORDER BY score DESC
