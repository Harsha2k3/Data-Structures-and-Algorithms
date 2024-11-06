class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        def isValid(row , col , c):

            for i in range(9):

                if board[i][col] == c:
                    return False
                
                if board[row][i] == c:
                    return False
                
            
            start_row , start_col = 3 * (row // 3) , 3 * (col // 3)

            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == c:
                        return False
            
            return True

        def rec():

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        for c in "123456789":
                            if isValid(i , j , c):
                                board[i][j] = c
                                if rec():
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True

        rec()