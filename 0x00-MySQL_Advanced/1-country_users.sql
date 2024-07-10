-- Create a table users with id, email, name
-- and enumeration of countries, default is the first country
CREATE TABLE IF NOT EXISTS users(
  id      INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  email   VARCHAR(255) NOT NULL UNIQUE,
  name    VARCHAR(255),
  country ENUM('US', 'CO', 'TN') NOT NULL
);
