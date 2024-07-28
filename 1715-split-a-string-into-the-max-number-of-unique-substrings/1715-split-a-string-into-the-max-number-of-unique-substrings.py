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
        set_ = set()

        def rec(ind):

            nonlocal res

            if ind == len(s):
                res = max(res , len(set_))
                return

            for i in range(ind , len(s)):
                if s[ind : i + 1] not in set_:
                    set_.add(s[ind : i + 1])
                    rec(i + 1)
                    set_.remove(s[ind : i + 1])

        rec(0)

        return res