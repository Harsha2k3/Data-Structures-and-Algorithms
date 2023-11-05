class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
        i = 0
        e = 0
        o = 0

        while(n != 0):
            if(n & 1 == 1):
                if(i % 2 == 0):
                    e += 1
                else:
                    o += 1
            i += 1
            n = n >> 1

        return [e,o]