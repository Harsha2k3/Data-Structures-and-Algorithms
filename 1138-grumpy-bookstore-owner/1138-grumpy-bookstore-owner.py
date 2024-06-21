class Solution(object):
    def maxSatisfied(self, c, g, m):

        s = 0
        res = float("-inf")
        sum_ = 0

        for i in range(len(g)):
            if g[i] == 0:
                s += c[i]

        start = 0

        for end in range(len(g)):
            if g[end] == 1:
                sum_ += c[end]

            if end - start + 1 == m:
                res = max(res , s + sum_)
                if g[start]:
                    sum_ -= c[start]
                start += 1

        return res