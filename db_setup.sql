-- Prepare the development database on the MySQL server

-- create the development database if it doesn't already exist
 DROP DATABASE IF EXISTS `fg_db`;
 CREATE DATABASE IF NOT EXISTS `fg_db`;
 USE `fg_db`;

-- reduce pasword policy to low
SET GLOBAL validate_password.policy=LOW;

-- add new user and set a password
CREATE USER IF NOT EXISTS 'fg_dev'@'localhost' IDENTIFIED BY 'fg_dev_pwd';

-- grant privileges to users on the new database
GRANT ALL PRIVILEGES ON fg_db.* TO 'fg_dev'@'localhost';

-- grand select privilege to user on performance_schema
GRANT SELECT ON performance_schema.* TO 'fg_dev'@'localhost';

FLUSH PRIVILEGES;
