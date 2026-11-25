-- 1378. Replace Employee ID With The Unique Identifier · Easy · 02-joins · MySQL
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/
-- Task: Return each employee's unique_id and name, showing NULL if they have no unique_id.
-- Idea: LEFT JOIN Employees to EmployeeUNI on id so unmatched employees are preserved with NULL unique_id.
-- Gotchas: INNER JOIN drops employees without a unique_id; Employees must stay on the left of the LEFT JOIN.

SELECT eu.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS eu
  ON e.id = eu.id;
