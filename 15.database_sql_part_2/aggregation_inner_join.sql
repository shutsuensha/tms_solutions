SELECT 
    authors.first_name || ' ' || authors.last_name AS author_name,
    SUM(sales.quantity) AS total_books_sold
FROM 
    authors
INNER JOIN 
    books ON authors.id = books.author_id
INNER JOIN 
    sales ON books.id = sales.book_id
GROUP BY 
    authors.id
ORDER BY 
    total_books_sold DESC;