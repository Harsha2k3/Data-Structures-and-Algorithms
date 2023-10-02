class Solution:
    def removeTrailingZeros(self, n: str) -> str:

        res = ""
        l = []

        for i in range(len(n[::-1])):
            if(n[::-1][i] == "0"):
                continue
            else:
                j = i
                break
        
        return n[::-1][j:][::-1]