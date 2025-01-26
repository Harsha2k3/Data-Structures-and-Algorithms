class Solution:
    def letterCombinations(self, d: str) -> List[str]:

        if d == "":
            return []

        h = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
            }

        res = []

        def rec(ind , l):

            nonlocal res

            if len(l) == len(d):
                res.append("".join(l)) 
                return

            for i in h[d[ind]]:
                l.append(i)
                rec(ind + 1 , l)
                l.pop()
        
        rec(0 , [])

        return res