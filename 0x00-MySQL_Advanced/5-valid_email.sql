-- reset the attribute valid_email   when   the email changes
-- (SET)                          (TRIGGER)          (UPDATE)
CREATE TRIGGER reset_email_validation
BEFORE UPDATE
    ON users FOR EACH ROW
   SET NEW.valid_email = IF(STRCMP(NEW.email, OLD.email), 0, NEW.valid_email);
