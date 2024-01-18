-- Create the database
CREATE DATABASE IF NOT EXISTS book_database;
USE book_database;

-- Create the authors table
CREATE TABLE IF NOT EXISTS authors (
    author_id INT PRIMARY KEY AUTO_INCREMENT,
    author_name VARCHAR(100) NOT NULL
);

-- Create the genres table
CREATE TABLE IF NOT EXISTS genres (
    genre_id INT PRIMARY KEY AUTO_INCREMENT,
    genre_name VARCHAR(50) NOT NULL
);

-- Create the publishers table
CREATE TABLE IF NOT EXISTS publishers (
    publisher_id INT PRIMARY KEY AUTO_INCREMENT,
    publisher_name VARCHAR(100) NOT NULL
);

-- Create the books table
CREATE TABLE IF NOT EXISTS books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    author_id INT,
    genre_id INT,
    publisher_id INT,
    publication_year INT,
    ISBN VARCHAR(13) UNIQUE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id),
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id),
    FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
);

-- Insert sample data into authors table
INSERT INTO authors (author_name) VALUES
    ('John Doe'),
    ('Jane Smith'),
    ('Bob Johnson');

-- Insert sample data into genres table
INSERT INTO genres (genre_name) VALUES
    ('Fiction'),
    ('Non-fiction'),
    ('Mystery');

-- Insert sample data into publishers table
INSERT INTO publishers (publisher_name) VALUES
    ('Publisher A'),
    ('Publisher B'),
    ('Publisher C');

-- Insert sample data into books table
INSERT INTO books (title, author_id, genre_id, publisher_id, publication_year, ISBN) VALUES
    ('Book 1', 1, 1, 1, 2020, '1234567890123'),
    ('Book 2', 2, 2, 2, 2019, '2345678901234'),
    ('Book 3', 3, 3, 3, 2018, '3456789012345');
