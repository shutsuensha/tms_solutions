-- Добавление авторов в таблицу authors
INSERT INTO authors (first_name, last_name)
VALUES 
    ('George', 'Orwell'),
    ('J.K.', 'Rowling'),
    ('J.R.R.', 'Tolkien'),
    ('Stephen', 'King');


-- Добавление книг в таблицу books
INSERT INTO books (title, author_id, publication_year)
VALUES 
    ('1984', 1, 1949),
    ('Animal Farm', 1, 1945),
    ('Harry Potter and the Philosopher`s Stone', 2, 1997),
    ('The Hobbit', 3, 1937),
    ('The Lord of the Rings', 3, 1954),
    ('Unknown Book', NULL, 2024);


-- Добавление продаж в таблицу sales
INSERT INTO sales (book_id, quantity)
VALUES 
    (1, 120),
    (2, 85),
    (3, 300),
    (4, 50),
    (5, 75);