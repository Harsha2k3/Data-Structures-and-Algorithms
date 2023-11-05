class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:

        xor = start ^ goal

        # Count number of 1's in xor
        # i.e, count the number of set bits

        count = 0

        while(xor != 0):
            if(xor & 1 == 1):
                count += 1
            xor = xor >> 1

        return count