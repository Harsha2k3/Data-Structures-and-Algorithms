class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        res = []

        def rec(l):

            nonlocal res

            if len(l) == n:
                res.append("".join(l))
                return

            if l and l[-1] == "0":
                l.append("1")
                rec(l)
                l.pop()
            
            if l and l[-1] == "1":
                l.append("0")
                rec(l)
                l.pop()

                l.append("1")
                rec(l)
                l.pop()
        
        rec(["0"])
        rec(["1"])

        return res