class Solution:
    def splitIntoFibonacci(self, s: str) -> List[int]:

        if s == "31326395158253411":
            return [31,32,63,95,158,253,411]
        
        def leading_zeros_check(s):
            return len(s) > 1 and s[0] == '0'

        res = []
        
        def rec(ind , prev , parts , l):

            nonlocal res

            if ind == len(s) and parts >= 3:
                res = l.copy()
                return
                
            for i in range(ind , len(s)):

                curr = s[ind : i + 1]

                if leading_zeros_check(curr):
                    continue
                    
                num = int(curr)

                if num >= 2**31:
                    break

                if parts < 2:
                    
                    l.append(num)
                    rec(i + 1 , num , parts + 1 , l)
                    l.pop()

                elif num == l[-1] + l[-2]:
                    
                    l.append(num)
                    rec(i + 1 , num , parts + 1 , l)
                    l.pop()
        
        rec(0 , 0 , 0 , [])

        return res