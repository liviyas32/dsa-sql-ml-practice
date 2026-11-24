-- 0584. Find Customer Referee · Easy · 01-select-filter · MySQL
-- https://leetcode.com/problems/find-customer-referee/
-- Task: Return names of customers not referred by customer id 2.
-- Idea: Use referee_id <> 2 OR referee_id IS NULL (keeps referee_id indexable, unlike COALESCE).
-- Gotchas: Plain referee_id <> 2 drops NULL rows due to SQL 3-valued logic.

SELECT name
FROM Customer
WHERE referee_id <> 2
   OR referee_id IS NULL;
