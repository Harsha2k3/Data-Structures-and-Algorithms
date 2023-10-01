class Solution:
    def finalString(self, s: str) -> str:

        res = ""

        for i in range(len(s)):
            if(s[i] != "i"):
                res += s[i]
            else:
                res = res[0:i][::-1]
        
        return res