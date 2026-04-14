CREATE DATABASE ticket_system;
USE ticket_system;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE
);
CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    status VARCHAR(20) DEFAULT 'Open',
    user_id INT,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);
INSERT INTO users(name, email) VALUES ('Ion Popa', 'ion_popa123@yahoo.com');
INSERT INTO users(name, email) VALUES ('Maria Iordache', 'iordache_m@gmail.com');
INSERT INTO tickets(title, description, user_id) VALUES('Login button is not working', 'When I press Login the page keeps loading', '1');
INSERT INTO tickets(title, description, user_id) VALUES('Wrong font color', 'On the contact page, the text is gray instead of black', '2');
