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
    name        VARCHAR(255)
);
```




## Links
[What are DDL DML...](https://stackoverflow.com/questions/2578194/what-are-ddl-and-dml#2578207)
[MySQL cheatsheet](https://devhints.io)

