class Solution:
    def solve(self, col, leftrow, upperDiagonal, lowerDiagonal, n):
        
        if col > n - 1:
            return 1
        # else:
        #     return 0

        count = 0

        for row in range(n):
            if leftrow[row] == 0 and lowerDiagonal[row+col] == 0 and upperDiagonal[n-1+col-row] == 0:
                leftrow[row] = 1
                lowerDiagonal[row+col] = 1
                upperDiagonal[n-1+col-row] = 1
                count += self.solve(col+1 , leftrow,upperDiagonal, lowerDiagonal, n)
                leftrow[row] = 0
                lowerDiagonal[row+col] = 0
                upperDiagonal[n-1+col-row] = 0

        return count


    def totalNQueens(self, n: int) -> int:
        
        leftrow = [0] * n
        upperDiagonal = [0] * (2 * n - 1)
        lowerDiagonal = [0] * (2 * n - 1)

        return self.solve(0, leftrow, upperDiagonal, lowerDiagonal, n)