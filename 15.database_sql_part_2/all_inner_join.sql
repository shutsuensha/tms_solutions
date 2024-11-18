SELECT 
    books.title AS book_title,
    books.publication_year AS public_year,
    authors.first_name || ' ' || authors.last_name AS author_name,
    sales.quantity AS sales_quantity
FROM 
    books
INNER JOIN 
    authors ON books.author_id = authors.id
INNER JOIN 
    sales ON books.id = sales.book_id;