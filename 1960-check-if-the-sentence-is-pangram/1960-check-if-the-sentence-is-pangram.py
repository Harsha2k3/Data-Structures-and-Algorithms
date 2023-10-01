class Solution:
    def checkIfPangram(self, s: str) -> bool:
        
        l = [chr(ord('a') + i) for i in range(26)]

        res = False

        for i in l:
            if(i in s):
                res = True
            else:
                res = False
                break

        return res