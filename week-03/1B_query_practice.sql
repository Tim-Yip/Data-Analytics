USE northwind;
-- 1. Write a query to list the product id, product name, and unit price of every product that Northwind sells. 
SELECT ProductID, ProductName, UnitPrice
FROM products;
-- 2. Write a query to identify the products where the unit price is $7.50 or less.
SELECT ProductID, ProductName, UnitPrice
FROM products
WHERE UnitPrice <= 7.5;
-- 3. What are the products that we carry where we have no units on hand, but 1 or more units are on backorder?
-- The product is Gorgonzola Telino with none in stock and 70 orders. 
SELECT ProductID, ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock = 0 AND UnitsOnOrder > 0;
-- 4. Examine the products table. How does it identify the type (category) of each item sold? Where can you find a list of all categories?
-- The products table lists categoryID. The categories are in the categories table. 
SELECT DISTINCT products.CategoryID, categories.CategoryName
FROM products
JOIN categories
ON products.CategoryID = categories.CategoryID;
--  5. Examine the products table again. How do you know what supplier each product comes from? Where can you find info on suppliers?
-- In the products table there is a supplierID. In the suppliers table there company names tied to the ID. 
SELECT products.SupplierID, suppliers.CompanyName, products.ProductName
FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
WHERE suppliers.CompanyName = 'Tokyo Traders';
-- 6. How many employees work at northwind? What employees have "manager" somewhere in their job title?
-- 9 employees work at northwind. 1 employee has manager in their job title named Steven Buchanan. 
SELECT COUNT(*) AS TotalEmployees
From employees;
SELECT EmployeeID, LastName, FirstName, Title
FROM employees
WHERE Title LIKE '%manager%';