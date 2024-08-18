# We have to write like Regular expression as we write in TOC

select * 
from Users
where mail regexp "^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$";

-- We use REGEXP (Regular expression) instead of LIKE for more complex pattern matching.
-- ^ ==> Indicates the start of the string.
-- [A-Za-z] ==> Email starts with a letter.
-- [A-Za-z0-9_.-]* ==> * allows for zero or more occurrences of letters, numbers, underscores, periods, or hyphens.
-- @leetcode\\.com ==> \\ is used to match a "."
-- $ ==> End of the string.