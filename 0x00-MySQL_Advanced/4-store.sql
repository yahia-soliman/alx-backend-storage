-- automatically decrease the quantity of an item  after adding a new order
-- (  TRIGGER  )(        UPDATE items            )(AFTER INSERT) (ON orders)
CREATE TRIGGER
    IF NOT EXISTS
       decrease_quantity_after_new_order
 AFTER INSERT
    ON orders
   FOR EACH ROW
   UPDATE items
      SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
