class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:

        # Create adjacency list for the graph
        graph = [[0 , 0]] + [[] for _ in range(n)]

        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)

        # graph = [[0, 0], [2, 3], [1, 3], [2, 1]]
        # [0,0] ==> For avoiding index errors
        # Neighbours of node 1 ==> 2 , 3
        # Neighbours of node 2 ==> 1 , 3
        # Neighbours of node 3 ==> 2 , 1
        
        print(graph)

        color = [0] * (n + 1)

        m = 4

        def isSafe(node , col):

            for n in graph[node]:
                if color[n] == col:
                    return False
            return True

        def rec(node):

            nonlocal graph , color , m , n

            if node == n + 1:
                return True

            for i in range(1 , m + 1):
                if isSafe(node , i):
                    color[node] = i
                    if rec(node + 1):
                        return True
                    color[node] = 0
            return False

        rec(1)

        return color[1:]