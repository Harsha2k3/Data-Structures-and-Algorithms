class Solution:
    def vowelStrings(self, w: List[str], l: int, r: int) -> int:

        res = 0
        o = ["a","e","i","o","u"]

        for i in w[l:r+1]:   
             if((i[0] in o) and (i[-1] in o)):
                 res += 1

        return res