class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        def rec(ind , l):

            nonlocal res
            
            if ind == len(s):
                res.append(l.copy())
                return

            for i in range(ind , len(s)):
                if s[ind : i + 1] == s[ind : i + 1][::-1]:
                    part = s[ind : i + 1]
                    l.append(part)
                    rec(i + 1 , l)
                    l.pop()
        
        rec(0 , [])

        return res