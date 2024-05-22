-- This script creates the table unique_id on the MySQL server. If the table already exists, the script will not fail.
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
