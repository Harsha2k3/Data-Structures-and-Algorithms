class Solution:
    def setZeroes(self, l: List[List[int]]) -> None:
        rows = []
        cols = []

        for i in range(len(l)):
            for j in range(len(l[0])):
                if l[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        for row in rows:
            l[row] = [0] * len(l[0])

        for col in cols:
            for i in range(len(l)):
                l[i][col] = 0
        
        return l