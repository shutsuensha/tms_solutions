SELECT 
    books.title AS book_title,
    SUM(sales.quantity) AS total_books_sold
FROM 
    books
INNER JOIN 
    sales ON books.id = sales.book_id
GROUP BY 
    books.id
HAVING 
    SUM(sales.quantity) > (
        SELECT 
            AVG(total_sales)
        FROM (
            SELECT 
                books.id AS book_id,
                SUM(sales.quantity) AS total_sales
            FROM 
                books
            INNER JOIN 
                sales ON books.id = sales.book_id
            GROUP BY 
                books.id
        ) AS subquery
    );
