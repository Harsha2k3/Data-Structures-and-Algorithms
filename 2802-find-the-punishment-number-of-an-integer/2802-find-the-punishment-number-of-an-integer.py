class Solution:
    def punishmentNumber(self, n: int) -> int:

        def rec(ind , s , target):

            if ind == len(s):
                return target == 0

            for i in range(ind , len(s)):

                left = s[ind : i + 1]

                if int(left) <= target:
                    if rec(i + 1 , s , target - int(left)):
                        return True
            
            return False


        res = 0

        for i in range(1 , n + 1):
            if rec(0 , str(i * i) , i):
                res += i * i
        
        return res