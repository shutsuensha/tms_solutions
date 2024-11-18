SELECT 
    authors.first_name || ' ' || authors.last_name AS author_name,
    COALESCE(SUM(sales.quantity), 0) AS total_books_sold
FROM 
    authors
LEFT JOIN 
    books ON authors.id = books.author_id
LEFT JOIN 
    sales ON books.id = sales.book_id
GROUP BY 
    authors.id
ORDER BY 
    total_books_sold DESC;