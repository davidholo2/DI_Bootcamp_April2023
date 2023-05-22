-- select * from customer;

-- SELECT CONCAT(first_name, ' ', last_name) AS full_name
-- FROM custom;

-- SELECT DISTINCT create_date
-- FROM customer;

-- select * from customer order by first_name desc

-- SELECT film_id, title, description, release_year, rental_rate
-- FROM film
-- ORDER BY rental_rate ASC;

-- select address,phone
-- from address where district='Texas'

-- select * from film where film_ID =15 OR film_ID=150

-- SELECT * FROM film where title='lion king'

-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title LIKE 'Li%';

-- SELECT *
-- FROM film
-- ORDER BY rental_rate ASC
-- LIMIT 10;

-- SELECT *
-- FROM film
-- ORDER BY rental_rate ASC
-- OFFSET 10 FETCH NEXT 10 ROWS ONLY;

-- SELECT c.first_name, c.last_name, p.amount, p.payment_date
-- FROM customer AS c
-- JOIN payment AS p ON c.customer_id = p.customer_id
-- ORDER BY c.customer_id;

-- SELECT film_id,title
-- FROM film WHERE film_id NOT IN(SELECT DISTINCT film_id FROM inventory);

-- SELECT city.city_id, city.city, country.country
-- FROM city
-- JOIN country ON city.country_id = country.country_id;

SELECT c.customer_id, CONCAT(c.first_name, ' ', c.last_name) AS customer_full_name, p.amount, p.payment_date, CONCAT(s.first_name, ' ', s.last_name) AS staff_full_name
FROM customer AS c
JOIN payment AS p ON c.customer_id = p.customer_id
JOIN staff AS s ON p.staff_id = s.staff_id
ORDER BY s.staff_id DESC;







