-- CREATE TABLE items (
--     item_id SERIAL PRIMARY KEY,
--     item VARCHAR(100) NOT NULL,
--     price FLOAT NOT NULL
-- );

-- CREATE TABLE customers (
--     cus_id SERIAL PRIMARY KEY,
--     first_name VARCHAR(100) NOT NULL,
--     last_name VARCHAR(100) NOT NULL
-- );

-- INSERT INTO items (item, price)
-- VALUES ('Small Desk', 100),
--        ('Large Desk', 300),
--        ('Fan', 80);

-- INSERT INTO customers (first_name, last_name)
-- VALUES ('Greg', 'Jones'),
--        ('Sandra', 'Jones'),
--        ('Scott', 'Scott'),
--        ('Trevor', 'Green'),
--        ('Melanie', 'Johnson');

SELECT * FROM items;
select * from items where price>80;
select * from items where price <=300;
SELECT * FROM customers WHERE last_name = 'Smith';
SELECT * FROM customers WHERE last_name = 'Jones';
SELECT * FROM customers WHERE first_name != 'Scott';


