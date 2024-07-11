## Triggers
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

## Links

[MySQL 8.4 Reference Manual :: 27.3.1 Trigger Syntax and Examples](https://dev.mysql.com/doc/refman/8.4/en/trigger-syntax.html)

[MySQL 8.4 Reference Manual :: 15.1.22 CREATE TRIGGER Statement](https://dev.mysql.com/doc/refman/8.4/en/create-trigger.html)
