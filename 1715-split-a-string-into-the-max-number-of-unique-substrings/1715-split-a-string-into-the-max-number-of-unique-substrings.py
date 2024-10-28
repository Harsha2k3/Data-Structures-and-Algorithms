class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        # Try to split at every possible char
        # abab 
        # a,bab ; ab,ab ; aba,b ==> Level - 1 of recursion tree
        # Level - 2 of recursion tree (1st comma os fixed and try all possibilities for 2nd comma)
        # For a,bab ==> a,b,ab ; a,ba,b 
        # For ab,ab ==> ab,a,b
        # For aba,b ==> aba,b

        res = 0
        se = set()

        def rec(ind):

            nonlocal res
            
            if ind == len(s):
                res = max(res , len(se))
                return

            for i in range(ind , len(s)):
                
                str_ = s[ind : i + 1]

                if str_ not in se:
                    se.add(str_)
                    rec(i + 1)
                    se.remove(str_)
        
        rec(0)

        return res