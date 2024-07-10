-- Create a table users with id, email, name
-- if the table exists the script will do nothing
CREATE TABLE IF NOT EXISTS users(
  id    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email VARCHAR(255) NOT NULL UNIQUE,
  name  VARCHAR(255)
);
