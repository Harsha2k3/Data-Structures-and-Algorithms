class Solution:
    def totalNQueens(self, n: int) -> int:

        count = 0

        lr = [0] * n                # Left row
        ud = [0] * (2 * n - 1)      # Upper diagonal
        ld = [0] * (2 * n - 1)      # Lower diagonal


        def solve(col):

            nonlocal count , lr , ud , ld

            if col == n:
                count += 1
                return

            for row in range(n):
                if lr[row] == 0 and ud[row + col] == 0 and ld[n - 1 + col - row] == 0:
                    lr[row] = 1
                    ud[row + col] = 1
                    ld[n - 1 + col - row] = 1
                    solve(col + 1)
                    lr[row] = 0
                    ud[row + col] = 0
                    ld[n - 1 + col - row] = 0

        solve(0)

        return count