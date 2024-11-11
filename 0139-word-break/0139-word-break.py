class Solution:
    def wordBreak(self, s: str, d: List[str]) -> bool:

        @lru_cache(None)
        def rec(ind):

            if ind == len(s):
                return True

            for i in range(ind , len(s)):
                if s[ind : i + 1] in d:
                    if rec(i + 1):
                        return True
            return False
        
        return rec(0)