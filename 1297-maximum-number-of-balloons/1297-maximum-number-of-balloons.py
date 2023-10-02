class Solution:
    def maxNumberOfBalloons(self, t: str) -> int:

        l = []

        for i in set("balloon"):
            if(i != "l" and i != "o"):
                l.append(t.count(i))
            else:
                l.append(int(t.count(i)/2))

        return min(l)