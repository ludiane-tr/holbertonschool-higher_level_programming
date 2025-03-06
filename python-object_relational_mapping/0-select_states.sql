-- Script to create the database and table 'states' with sample data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;

-- Create the 'states' table
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT,  -- Auto-incremented primary key
    name VARCHAR(256) NOT NULL,      -- State name (max 256 characters)
    PRIMARY KEY (id)                 -- Set 'id' as primary key
);

-- Insert test data into 'states' table
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
