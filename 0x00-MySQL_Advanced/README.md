# MySQL
MySQL is a relational database management system, let us know how to use it as a backend engineers

## Installing 
MySQL is available as mariadb in most linux distros, or you can easily use it with docker.

```sh
docker run --name <NAME_IT> -e MYSQL_ROOT_PASSWORD=<SOMETHING> -d mysql:<TAG>
```


## Using MySQL
So we need to play with MySQL a little bit.

for the first time we only have the root user so in the terminal we say
```sh
mysql -uroot -p
```

this will ask for the root password and will give us a new prompt `mysql> ` which we can write SQL statements to
```mysql
bash-5.1# mysql -uroot -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
wners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>

```

another way to run SQL code is to pass the file with the statements to `mysql` command
```sh
mysql -uroot -p  [DB_NAME] < db_dump.sql
```
```sh
# OR THIS
cat db_dump.sql | mysql -uroot -p  [DB_NAME]
```

## DDL with MySQL
DDL means Data Definition Language and it is the set of SQL statements that deals with manipulating data definitions or metadata like creating, dropping, altering, or renaming databases and tables.

With DDL we draw the shape of our database, we define the charactarestics of the data inside the tables.

```sql
-- this is a comment
-- let us create our first awesome database
CREATE DATABASE IF NOT EXISTS awesome_db;

-- and our first table will be for the awesome users
CREATE TABLE IF NOT EXISTS awesome_db.users (
    -- here we define columns
  --col_name    data_type       other_characteristics
    id          INT             NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email       VARCHAR(255)    NOT NULL UNIQUE,
    name        VARCHAR(255),
    gender      ENUM('M', 'F')  NOT NULL        -- NOT NULL makes the default 'M' (the first value)
);
```


## DRL/DQL with MySQL
Data Retrieval/Query Language is the subset of commands helps to GET data from the database in many forms, and we will do all of that with the SELECT command

```sql
-- List all columns from the users table without any filtering (all rows also)
SELECT * FROM users;

-- List (all origins of metal bands) and (total number of fans for bands in that origin)
-- Sort/oreder the result by the number of fans descending
SELECT origin, SUM(fans) as nb_fans
  FROM metal_bands
 GROUP BY origin
 ORDER BY nb_fans DESC;

-- List brand_name and lifespan of all brands with Glam rock as one of thier styles,
-- sort the results with lifespan from heighest to lowest (descending)
-- NOTE: if the band is split then the lifespan = split year - formation year
--                                else lifespan = 2022 - formation year
SELECT band_name, IF(split, split - formed, 2022 - formed) as lifespan
  FROM metal_bands
 WHERE style LIKE '%Glam rock%'
 ORDER BY lifespan DESC;
```


## Triggers in MySQL
Back to DDL, triggers helps to automatically change some data in a a table based on changes in another table, they are user specified actions that fire when a specific change (INSERT, UPDATE, DELETE) happens to the data.


    Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!
    - Holberton wiseman


```sql
-- automatically decrease the quantity (UPDATE) of an item after (AFTER) adding (INSERT) a new order

CREATE TRIGGER
    IF NOT EXISTS
       decrease_quantity_after_new_order
 AFTER INSERT
    ON orders
   FOR EACH ROW

   UPDATE items
      SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
```

Now this is part of the orders table

## Links
[What are DDL DML...](https://stackoverflow.com/questions/2578194/what-are-ddl-and-dml#2578207)
[MySQL cheatsheet](https://devhints.io)

