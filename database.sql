CREATE DATABASE ticket_system;
USE ticket_system;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(25) NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    user_id INT,
    status VARCHAR(50) DEFAULT 'Open',
    FOREIGN KEY (user_id) REFERENCES users(id)
);
