class Solution:
    def countSeniors(self, d: List[str]) -> int:

        res = 0

        for i in d:
            if(int(i[11:13]) > 60):
                res += 1

        return res