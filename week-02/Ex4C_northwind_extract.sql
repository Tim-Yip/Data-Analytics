/*
a) What is the name of the table that holds the items Northwind sells?
The products table contains all the products sold. 
b) What is the name of the table that holds the types/categories of the items Northwind sells?
The categories table holds the category names of the items. 
*/
SELECT * FROM employees;
/*
a) Who is the Northwind employee whose name makes it look like she’s a bird?
The name of the employee is Margaret Peacock.
*/
SELECT * FROM products;
/*
a) How many records does your query return? Using the toolbar options at the top of
the query pane, how can you change your query to retrieve only 10 rows?
It returned 77 records. There is a drop down to change the limit of rows returned with multiple options one of them being limit to 10 rows. 
*/
SELECT * FROM categories;
/*
c) What is the category id of seafood?
The category id for seafood is 8.
*/
SELECT OrderID, OrderDate, ShipName, ShipCountry
FROM orders
LIMIT 50;