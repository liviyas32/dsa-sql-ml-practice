-- 1148. Article Views I · Easy · 01-select-filter · MySQL
-- https://leetcode.com/problems/article-views-i/
-- Task: Find authors who viewed at least one of their own articles, sorted ascending.
-- Idea: Match viewer_id = author_id, deduplicate with DISTINCT, alias as id, and sort by id.
-- Gotchas: Same author can self-view multiple times, so DISTINCT is required; ORDER BY can use the SELECT alias.

SELECT DISTINCT author_id AS id
FROM Views
WHERE viewer_id = author_id
ORDER BY id ASC;
