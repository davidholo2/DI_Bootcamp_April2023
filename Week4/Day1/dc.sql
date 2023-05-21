-- CREATE TABLE actor (
--     actor_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100) NOT NULL,
--     date_birth DATE NOT NULL,
--     number_oscars SMALLINT NOT NULL DEFAULT 0
-- )

-- -- SELECT all the columns from the table
-- SELECT * FROM actor;

-- SELECT first_name, last_name FROM actor;

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES ('Georges', 'Clooney', '1976-03-12', 2);

-- SELECT * FROM actor;

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES ('Patrick', 'Jolie', '1980-04-22', 1);

-- SELECT first_name, last_name FROM actor;

-- -- select only the actor which first name is Angelina
-- SELECT first_name, last_name FROM actor WHERE first_name = 'Angelina';

-- -- select the actor which first name is Angelina or last name is Clooney
-- SELECT first_name, last_name FROM actor WHERE first_name = 'Angelina' OR last_name = 'Clooney';

-- -- empty result
-- SELECT first_name, last_name FROM actor WHERE first_name = 'Angelina' AND last_name = 'Clooney';

-- SELECT first_name, last_name FROM actor WHERE number_oscars >= 2;

-- -- show the actors in ascending alphabetical order of the last name
-- SELECT * FROM actor ORDER BY last_name ASC;

-- SELECT * FROM actor ORDER BY last_name ASC, first_name DESC;

-- -- OLDEST - limit 1 the first one appearing
-- SELECT * FROM actor ORDER BY date_birth ASC LIMIT 1;

-- -- born after THE YEAR 1980
-- SELECT * FROM actor WHERE EXTRACT(YEAR from date_birth) >= 1980;

-- -- select the actors that have the letter A in their first name
-- SELECT * FROM actor WHERE first_name LIKE '%A%';

-- -- select the actors that have the letter a in their first name
-- SELECT * FROM actor WHERE first_name LIKE '%a%';

-- -- CASE insensitive
-- SELECT * FROM actor WHERE first_name ILIKE '%A%';

-- -- update the actor and return the row that was modified
-- UPDATE actor
-- SET last_name = 'Clooney'
-- WHERE actor_id = 1
-- RETURNING *;

-- -- without WHERE: update everything
-- UPDATE actor
-- SET number_oscars = 3
-- RETURNING *;

-- UPDATE actor
-- SET number_oscars = 5
-- WHERE last_name = 'Clooney'
-- RETURNING *;

-- SELECT * FROM actor ORDER BY actor_id;

-- -- show you the record that was deleted
-- DELETE FROM actor
-- WHERE actor_id = 6
-- RETURNING *;

-- INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
-- VALUES ('John', 'Jolie', '1980-04-22', 1)
-- RETURNING *;

-- -- add a new column to the actor table
-- ALTER TABLE actor ADD COLUMN salary INTEGER;
-- ALTER TABLE actor ADD COLUMN nationality VARCHAR(200);

-- SELECT * FROM actor;

-- -- UPDATE ALL THE ACTORS 1000000 * their number of oscars
-- UPDATE actor
-- SET salary = 1000000 * number_oscars
-- RETURNING *;

-- UPDATE actor
-- SET nationality = 'American'
-- WHERE actor_id IN (1,2,3)
-- RETURNING *;

-- -- update the nationality of the actors which actor id is 4 or 7
-- UPDATE actor
-- SET nationality = 'French'
-- WHERE actor_id IN (4,7)
-- RETURNING *;

-- -- update the nationality of the actors which actor id is below 7
-- UPDATE actor
-- SET nationality = 'Israeli'
-- WHERE actor_id < 7
-- RETURNING *;

-- -- update the nationality of the actors which actor id is between 1 and 3
-- UPDATE actor
-- SET nationality = 'Chinese'
-- WHERE actor_id BETWEEN 1 AND 3
-- RETURNING *;

SELECT COUNT(*) FROM actor;
INSERT INTO actor (first_name, last_name, date_birth, number_oscars) VALUES ();
SELECT COUNT(*) FROM actor;
