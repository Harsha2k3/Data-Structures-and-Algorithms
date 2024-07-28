class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []

        def rec(l):
            if len(l) == n:
                if l[0] != 0:
                    res.append(int(''.join(map(str, l))))
                return

            for i in range(10):
                if l and (abs(l[-1] - i) == k):
                    l.append(i)
                    rec(l)
                    l.pop()
                elif not l:
                    l.append(i)
                    rec(l)
                    l.pop()

        for i in range(1, 10):
            rec([i])

        return res