class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        xor = 0

        for i in s:
            xor ^= ord(i)
        
        for i in t:
            xor ^= ord(i)

        return chr(xor)

        # Get all the ascii values of the char's in s and t
        # Apply XOR between all of them
        # The remaining ascii value's char is the result that is required