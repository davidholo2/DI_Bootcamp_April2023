CREATE TABLE actor (
    actor_id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    date_birth DATE NOT NULL,
    number_oscars SMALLINT NOT NULL DEFAULT 0
)


-- SELECT all the columns from the table
SELECT * FROM actor

SELECT first_name, last_name FROM actor

INSERT INTO actor (first_name, last_name, date_birth, number_oscars)
VALUES ('Georges', 'Cloney', '1976-03-12', 2)

SELECT * FROM actor