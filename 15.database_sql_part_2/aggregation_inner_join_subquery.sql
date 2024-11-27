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
HAVING 
    SUM(sales.quantity) = (
        SELECT 
            MAX(total_sales)
        FROM (
            SELECT 
                authors.id AS author_id,
                SUM(sales.quantity) AS total_sales
            FROM 
                authors
            INNER JOIN 
                books ON authors.id = books.author_id
            INNER JOIN 
                sales ON books.id = sales.book_id
            GROUP BY 
                authors.id
        ) AS subquery
    );