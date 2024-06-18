class Solution:
    def wordBreak(self, s: str, d: List[str]) -> bool:

        # d = set(dic)
        
        @lru_cache(None)
        def rec(i):

            if i == len(s):
                return True

            res = False

            for j in range(i ,len(s)):
                # if s[i:j+1] can be found
                # we continue moving to next substring s[j+1:]
                if s[i:j+1] in d:
                    res =  rec(j+1) or res
            
            return res

        return rec(0)


        # i = 0
        # So, j starts from i ==> j = 0
        # l ==> Not in d (Dict) ,  So j = 1
        # le ==> Not in d , So j = 2
        # lee ==> Not in d , So j = 3
        # leet ==> Present in d, So we will search from next word
        # For that we pass j + 1
        # Now new i = j + 1
        # Same process is repeated