-- This script creates the table force_name on the MySQL server. If the table already exists, the script will not fail.
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
