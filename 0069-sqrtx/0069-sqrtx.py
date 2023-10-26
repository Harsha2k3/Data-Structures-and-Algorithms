class Solution:
    def mySqrt(self, n: int) -> int:
        
        if(n == 1):
            return 1
        s = 0
        e = n

        while(s <= e):
            m = int((s + e)/2)
            if(m * m == n):
                return m
            if(m * m > n):
                e = m - 1
            else:
                s = m + 1
                
        return e