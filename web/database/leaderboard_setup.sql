DROP DATABASE IF EXISTS leaderboard;
CREATE DATABASE IF NOT EXISTS leaderboard;
USE leaderboard;

-- Create table
CREATE TABLE leaderboard (
                             id INT AUTO_INCREMENT PRIMARY KEY,
                             name VARCHAR(100) NOT NULL UNIQUE,
                             matches INT DEFAULT 0,
                             wins INT DEFAULT 0,
                             losses INT DEFAULT 0);