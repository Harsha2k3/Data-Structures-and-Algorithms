class Solution:
    def longestPalindrome(self, s: str) -> int:

        seen = set()
        res = 0

        for i in s:
            if i in seen:
                seen.remove(i)
                res += 2
            else:
                seen.add(i)

        return res + 1 if seen else res