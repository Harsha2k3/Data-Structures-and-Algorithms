class Solution:
    def mySqrt(self, x: int) -> int:

        num = 1
        while num * num <= x:
            num += 1
            
        return (num - 1)