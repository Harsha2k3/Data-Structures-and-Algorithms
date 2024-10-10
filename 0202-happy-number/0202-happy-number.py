class Solution:
    def isHappy(self, n: int) -> bool:
        
        ns = str(n)
        s = set()

        while True:

            res = 0

            for i in ns:
                res += int(i) ** 2
            
            if res == 1:
                return True

            if res in s:
                return False
            else:
                s.add(res)
            
            ns = str(res)