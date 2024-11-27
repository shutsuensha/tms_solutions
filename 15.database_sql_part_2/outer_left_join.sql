SELECT 
    COALESCE(authors.first_name || ' ' || authors.last_name, 'No Author') AS author_name,
    COALESCE(books.title, 'No Book') AS book_title,
    COALESCE(sales.quantity, 0) AS sales_quantity
FROM 
    books
FULL OUTER JOIN 
    authors ON books.author_id = authors.id
LEFT JOIN 
    sales ON books.id = sales.book_id;
