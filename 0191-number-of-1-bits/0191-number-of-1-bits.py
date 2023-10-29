class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # n = int("0b" + str(n) , 2)

        count = 0

        while(n != 0):
            if(n & 1 == 1):
                count += 1
            n = n >> 1

        return count