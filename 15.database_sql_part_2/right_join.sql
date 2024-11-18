SELECT 
    authors.first_name || ' ' || authors.last_name AS author_name,
    books.title AS book_title,
    books.publication_year AS public_year
FROM 
    authors
RIGHT JOIN 
    books
ON 
    authors.id = books.author_id;
