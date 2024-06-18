class Solution:

    # Optimized Approach
    
    def solve(self, ind, i, j, a, n, vis, di, dj, word):
        
        if ind == len(word) - 1:
            return True
        
        dir = "DLRU"
        
        for inde in range(4):
            nexti = i + di[inde]
            nextj = j + dj[inde]
            if nexti >= 0 and nextj >= 0 and nexti < n and nextj < len(a[0]) and not vis[nexti][nextj] and ind + 1 < len(word) and a[nexti][nextj] == word[ind + 1]:
                vis[i][j] = 1
                if self.solve(ind + 1, nexti, nextj, a, n, vis, di, dj, word):
                    return True
                vis[i][j] = 0
        return False


    def exist(self, m : List[List[str]], word: str) -> bool:
        
        ans = []

        n = len(m)
        
        vis = [[0 for _ in range(len(m[0]))] for _ in range(n)]
        
        # (i , j)
        # Down  ==> (i + 1 , j) 
        # Left  ==> (i , j - 1)
        # Right ==> (i , j + 1)
        # Up    ==> (i - 1 , j)
        
        di = [+1, 0, 0, -1]    
        dj = [0, -1, 1, 0]

        for i in range(len(m)):
            for j in range(len(m[0])):
                if m[i][j] == word[0] and self.solve(0, i, j, m, n, vis, di, dj, word):
                    return True
        return False