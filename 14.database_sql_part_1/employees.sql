DROP TABLE IF EXISTS Employees;


CREATE TABLE Employees (
    id SERIAL PRIMARY KEY,          
    Name VARCHAR(255) NOT NULL,      
    Position VARCHAR(255) NOT NULL,    
    Department VARCHAR(255) NOT NULL,   
    Salary NUMERIC(10, 2) NOT NULL  
);


INSERT INTO Employees (Name, Position, Department, Salary)
VALUES
    ('Daniil Kupryianchyk', 'Backend Developer', 'IT', 5500.00),
    ('Anna Ivanova', 'UI/UX Designer', 'Design', 4500.00),
    ('Sergey Petrov', 'Frontend Developer', 'IT', 5000.00),
    ('Elena Smirnova', 'HR Specialist', 'HR', 4000.00),
    ('Viktor Kolesnikov', 'Project Manager', 'Management', 6000.00);


UPDATE Employees
SET Position = 'Lead Frontend Developer', Salary = 6500.00
WHERE Name = 'Sergey Petrov';


ALTER TABLE Employees
ADD COLUMN HireDate DATE;


UPDATE Employees
SET HireDate = CASE
    WHEN id = 1 THEN DATE '2022-01-15'
    WHEN id = 2 THEN DATE '2023-03-20'
    WHEN id = 3 THEN DATE '2021-11-10'
    WHEN id = 4 THEN DATE '2020-07-05'
    WHEN id = 5 THEN DATE '2019-09-30'
    ELSE DATE '2022-06-01'
END
WHERE HireDate IS NULL;


SELECT * 
FROM Employees
WHERE Position = 'Manager';


SELECT * 
FROM Employees
WHERE Salary > 5000;


SELECT * 
FROM Employees
WHERE Department = 'Sales';


SELECT ROUND(avg(Salary), 2) as average_Employees_salary
FROM Employees;


DROP TABLE IF EXISTS Employees;