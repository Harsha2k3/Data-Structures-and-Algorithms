class Solution:
    def repeatedCharacter(self, s: str) -> str:

        l = []
        count = 0
        res = ""

        for i in range(len(s)):
            if (s[i] in set(s[0:i])):
                res = s[i]
                break


        return res