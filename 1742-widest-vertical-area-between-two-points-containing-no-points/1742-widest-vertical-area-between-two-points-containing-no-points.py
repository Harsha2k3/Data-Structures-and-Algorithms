class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        res = []

        p = sorted(points , key = lambda x: x[0])

        for i in range(1,len(p)):
            res.append(p[i][0]-p[i-1][0])

        return max(res)        