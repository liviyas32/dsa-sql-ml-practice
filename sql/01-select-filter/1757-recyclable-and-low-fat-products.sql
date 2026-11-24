-- 1757. Recyclable and Low Fat Products · Easy · 01-select-filter · MySQL
-- https://leetcode.com/problems/recyclable-and-low-fat-products/
-- Task: Return product IDs that are both low fat and recyclable.
-- Idea: Filter rows in WHERE with AND on both enum flag columns.
-- Gotchas: None; direct match on both flags.

SELECT product_id
FROM Products
WHERE low_fats = 'Y'
  AND recyclable = 'Y';
