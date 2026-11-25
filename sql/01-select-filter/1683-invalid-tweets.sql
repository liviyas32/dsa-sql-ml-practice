-- 1683. Invalid Tweets · Easy · 01-select-filter · MySQL
-- https://leetcode.com/problems/invalid-tweets/
-- Task: Return IDs of tweets whose content has strictly more than 15 characters.
-- Idea: Filter rows in WHERE using CHAR_LENGTH(content) > 15.
-- Gotchas: In MySQL, LENGTH() counts bytes while CHAR_LENGTH() counts characters (matters for UTF-8/emojis); bound is strictly > 15.

SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
