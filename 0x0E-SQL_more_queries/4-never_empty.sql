-- This script creates the table id_not_null on the MySQL server. If the table already exists, the script will not fail.
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
