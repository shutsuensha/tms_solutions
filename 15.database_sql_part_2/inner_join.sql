SELECT 
    books.title AS book_title,
    books.publication_year as public_year,
    authors.first_name || ' ' || authors.last_name AS author_name
FROM 
    books
INNER JOIN 
    authors
ON 
    books.author_id = authors.id;