class Solution:
    def similarPairs(self, w: List[str]) -> int:

        res = 0

        for i in range(len(w)):
            for j in range(len(w)):
                if(set(w[i]) == set(w[j]) and i != j):
                    res += 1

        return int(res/2)