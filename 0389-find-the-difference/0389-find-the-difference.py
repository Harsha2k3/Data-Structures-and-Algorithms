class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        xor = 0

        for i in s:
            xor ^= ord(i)
        
        for i in t:
            xor ^= ord(i)

        return chr(xor)