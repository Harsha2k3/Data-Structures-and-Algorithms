class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        def isbal(num):

            freq = [0] * 10

            while num > 0:
                d = num % 10
                if d == 0:
                    return False
                freq[d] += 1
                num //= 10
            
            for i in range(len(freq)):
                if freq[i] != 0 and freq[i] != i:
                    return False
            return True

        while True:

            n += 1
            if isbal(n): return n