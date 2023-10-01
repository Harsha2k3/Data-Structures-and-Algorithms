class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        return str(bin(n)) == str(bin(n))[::-1]