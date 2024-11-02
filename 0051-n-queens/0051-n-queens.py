class Solution:

    # https://haseebq.com/n-queens-visualizer/

    # Optimized code
    # This takes O(1) T.C for checking previous queens
    # We will use hashmap for achieving this

    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []

        board = ["." * n for i in range(n)]

        lr = [0] * n                # Left row
        ud = [0] * (2 * n - 1)      # Upper diagonal
        ld = [0] * (2 * n - 1)      # Lower diagonal


        def solve(col):

            nonlocal res , board , lr , ud , ld

            if col == n:
                res.append(board.copy())
                return

            for row in range(n):
                if lr[row] == 0 and ud[row + col] == 0 and ld[n - 1 + col - row] == 0:
                    board[row] = board[row][:col] + "Q" + board[row][col + 1 : ]
                    lr[row] = 1
                    ud[row + col] = 1
                    ld[n - 1 + col - row] = 1
                    solve(col + 1)
                    board[row] = board[row][:col] + "." + board[row][col + 1 : ]
                    lr[row] = 0
                    ud[row + col] = 0
                    ld[n - 1 + col - row] = 0

        solve(0)

        return res



    # # This is not optimized
    # # Beacuse, we are taking extra O(n) T.C for checking previous queens (For isSafe function) 


    # def solveNQueens(self, n: int) -> List[List[str]]:

    #     res = []

    #     board = ["." * n for i in range(n)]

    #     def isSafe(row , col):

    #         nonlocal res , board

    #         duprow = row
    #         dupcol = col

    #         # Upper left diagonal

    #         while row >= 0 and col >= 0:
    #             if board[row][col] == "Q":
    #                 return False
    #             row -= 1
    #             col -= 1

    #         # Left row

    #         row = duprow
    #         col = dupcol
            
    #         while col >= 0:
    #             if board[row][col] == "Q":
    #                 return False
    #             col -= 1

    #         # Lower left diagonal

    #         row = duprow
    #         col = dupcol

    #         while row <= n - 1 and col >= 0:
    #             if board[row][col] == "Q":
    #                 return False
    #             row += 1
    #             col -= 1

    #         return True


    #     def solve(col):

    #         nonlocal res , board

    #         if col == n:
    #             res.append(board.copy())
    #             return

    #         for row in range(n):
    #             if isSafe(row , col):
    #                 board[row] = board[row][:col] + "Q" + board[row][col + 1 : ]
    #                 solve(col + 1)
    #                 board[row] = board[row][:col] + "." + board[row][col + 1 : ]

    #     solve(0)

    #     return res