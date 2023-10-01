class Solution:
    def maximumNumberOfStringPairs(self, w: List[str]) -> int:

        res = 0
        
        for i in range(len(w)):
            if(w.count(w[i]) == w.count(w[i][::-1]) and w[i].count(w[i][0]) != len(w[i])):
                res += w.count(w[i])

        return int(res/2)