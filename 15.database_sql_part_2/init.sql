-- Создание таблицы authors
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Создание таблицы books
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    author_id INT,
    publication_year INT NOT NULL,
    CONSTRAINT fk_author FOREIGN KEY (author_id) REFERENCES authors(id)
);

-- Создание таблицы sales
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity >= 0),
    CONSTRAINT fk_book FOREIGN KEY (book_id) REFERENCES books(id)
);