class Solution(object):
    def minimumArea(self, grid):
        
        m , n = len(grid) , len(grid[0])
        
        min_row , max_row = m , -1
        min_col , max_col = n , -1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        if max_row == -1 or max_col == -1:
            return 0

        length = max_col - min_col + 1
        breadth = max_row - min_row + 1

        return length * breadth