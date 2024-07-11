SELECT * FROM items;  -- 10 of each one
SELECT * FROM orders; -- empty

INSERT INTO orders (item_name, number) VALUES ('apple', 1);
INSERT INTO orders (item_name, number) VALUES ('apple', 3);
INSERT INTO orders (item_name, number) VALUES ('pear', 2);

SELECT "------------";

SELECT * FROM items;
SELECT * FROM orders;

-- vim: ft=sql
