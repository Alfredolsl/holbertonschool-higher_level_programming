-- lists all cities of california that can be found in db hbtn_0d_usa
SELECT id, name FROM cities WHERE state_id = (SELECT id from states WHERE name = 'California') ORDER BY id ASC;
