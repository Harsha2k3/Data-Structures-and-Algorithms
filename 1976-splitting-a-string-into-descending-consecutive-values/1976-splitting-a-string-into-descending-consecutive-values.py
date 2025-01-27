class Solution:
    def splitString(self, s: str) -> bool:
        
        def rec(ind , parts , prev):

            if ind == len(s):
                return parts >= 2

            for i in range(ind , len(s)):
                num = int(s[ind : i + 1])
                if prev == -100000 or prev - 1 == num:
                    if rec(i + 1 , parts + 1 , num):
                        return True
            
            return False

        return rec(0 , 0 , -100000)