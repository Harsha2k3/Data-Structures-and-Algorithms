class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        nRows, nCols = len(grid), len(grid[0])

        visited = set()

        def inBound(row, col):
            return 0 <= row < nRows and 0 <= col < nCols

        def dfs(row, col):

            if not inBound(row , col) or (row , col) in visited or grid[row][col] == 0:
                return 0

            visited.add((row, col))

            left = dfs(row , col - 1)
            right = dfs(row , col + 1)
            up = dfs(row - 1 , col)
            down = dfs(row + 1 , col)

            visited.remove((row , col))

            return grid[row][col] + max(left , right , up , down)

        maxGold = 0

        for row in range(nRows):
            for col in range(nCols):
                if grid[row][col] and (row, col) not in visited:
                    maxGold = max(maxGold , dfs(row , col))

        return maxGold