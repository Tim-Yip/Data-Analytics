USE northwind;
-- Write a query to find the price of the cheapest item that Northwind sells. Then write a
-- second query to find the name of the product that has that price.
SELECT MIN(UnitPrice)
FROM products;
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);
-- 2. Write a query to find the average price of all items that Northwind sells.
SELECT AVG(UnitPrice)
FROM products;
-- 3. Write a query to find the price of the most expensive item that Northwind sells. Then
-- write a second query to find the name of the product with that price, plus the name of
-- the supplier for that product.
SELECT MAX(UnitPrice)
FROM products;
SELECT products.ProductName, products.UnitPrice, suppliers.CompanyName
FROM products
JOIN suppliers
ON products.SupplierID = suppliers.SupplierID
WHERE products.UnitPrice = (SELECT MAX(UnitPrice) FROM products);
-- 4. Write a query to find total monthly payroll.
SELECT SUM(Salary)
FROM employees;
-- 5. Write a query to identify the highest salary and the lowest salary amounts which any employee makes.
SELECT MAX(Salary), MIN(Salary)
FROM employees;
-- 6. Write a query to find the name and supplier ID of each supplier and the number of items they supply.
SELECT suppliers.SupplierID, suppliers.CompanyName, COUNT(products.productID) TotalProducts
FROM suppliers
LEFT JOIN Products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.SupplierID, suppliers.CompanyName;
-- 7. Write a query to find the list of all category names and the average price for items in each category.
SELECT categories.CategoryName, AVG(products.UnitPrice) AvgPrice
FROM categories
JOIN products
ON categories.CategoryID = products.CategoryID
GROUP BY categories.CategoryID;
-- 8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
-- is the name of each supplier and the number of items they supply.
SELECT suppliers.CompanyName, COUNT(products.ProductID)
FROM suppliers
JOIN products
ON suppliers.SupplierID = products.SupplierID
GROUP BY suppliers.CompanyName
HAVING COUNT(products.ProductID) >= 5;
-- 9. Write a query to list products currently in inventory by the product id, product name,
-- and inventory value (calculated by multiplying unit price by the number of units on
-- hand). Sort the results in descending order by value. If two or more have the same
-- value, order by product name. If a product is not in stock, leave it off the list.
SELECT ProductID, ProductName, UnitPrice * UnitsInStock TotalValue
FROM products
WHERE UnitsInStock > 0
ORDER BY TotalValue DESC, ProductName ASC;