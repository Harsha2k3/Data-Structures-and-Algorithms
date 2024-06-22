class Solution(object):
    def getHappyString(self, n, k):

        res = []

        def rec(l):

            if len(res) == k:
                return

            if len(l) == n:
                res.append("".join(l))
                return

            for i in ["a" , "b" , "c"]:
                if not l or l[-1] != i:
                    l.append(i)
                    rec(l)
                    l.pop()

        rec([])

        return res[-1] if len(res) >= k else ""