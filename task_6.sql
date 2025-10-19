-- Switch to the correct database
USE alx_book_store;

-- Script that inserts multiple rows into the table customer
-- from the database passed as an argument

INSERT INTO customer (customer_id, customer_name, email, address)
VALUES
(2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness  Ave.'),
(3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness  Ave.'),
(4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness  Ave.');
