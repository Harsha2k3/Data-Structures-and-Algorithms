class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        rem = ""
        res = "" 

        for i in order:
            if(i in s):
                for j in range(s.count(i)):
                    res += i

        for i in s:
            if(i not in order):
                rem += i

        return res + rem