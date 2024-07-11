# Triggers
Back to DDL, triggers helps to automatically change some data in a a table based on changes in another table, they are user specified actions that fire when a specific change (INSERT, UPDATE, DELETE) happens to the data.


> Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!
> -- Holberton wiseman


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


# Procedures
in programming a procedure is a set of instructions labeled with a name and can be executed later, in MySQL we can create procedure to write some business logic into the database, the logic you can write with a procedure can be written in a with the programming language you are using for the back end, but having it with the data itself written in SQL makes it portable and easy to use with different programming languages and ORMs.

```sql
-- set custom delimeter
DELIMITER //

-- adds new correction for a student
CREATE PROCEDURE AddBonus (
         IN user_id INT,
         IN project_name VARCHAR(255),
         IN score INT
       )
BEGIN
  DECLARE project_id INT;

  -- get the project id
  set project_id = (SELECT id FROM projects WHERE name = project_name);

  -- create the project if it does not exists
  IF IF(project_id, 0, 1) THEN
    INSERT INTO projects (name)
    VALUES               (project_name);
    SET project_id = LAST_INSERT_ID();
  END IF;

  -- create the correction row
  INSERT INTO corrections (user_id, project_id, score)
  VALUES                  (user_id, project_id, score);

END //
DELIMITER ;
```

# Links

[MySQL 8.4 Reference Manual :: 27.3.1 Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.4/en/trigger-syntax.html)

[MySQL 8.4 Reference Manual :: 15.1.22 CREATE TRIGGER Statement](https://dev.mysql.com/doc/refman/8.4/en/create-trigger.html)

[MySQL 5.7 Reference Manual :: 12.1 Built-In Function and Operator](https://dev.mysql.com/doc/refman/5.7/en/built-in-function-reference.html)

[MySQL 5.7 Reference Manual :: 13.1.16 CREATE PROCEDURE and CREATE FUNCTION Statements](https://dev.mysql.com/doc/refman/5.7/en/create-procedure.html)
