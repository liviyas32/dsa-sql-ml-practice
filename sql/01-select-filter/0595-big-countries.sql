-- 0595. Big Countries · Easy · 01-select-filter · MySQL
-- https://leetcode.com/problems/big-countries/
-- Task: Return name, population, and area for countries meeting the area or population threshold.
-- Idea: Single WHERE filter with OR on the two inclusive (>=) thresholds.
-- Gotchas: Bounds are inclusive (>=, not >); on large indexed tables, UNION can outperform OR.

SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
