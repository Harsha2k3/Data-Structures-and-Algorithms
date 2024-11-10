class Solution:

    # Same as m - coloring problem in backtracking

    def isSafe(self, node, color, graph, col):

        for neighbor in graph[node]:
            if color[neighbor] == col:
                return False
        return True

    def solve(self, node, color, m, N, graph):

        if node == N + 1:
            return True

        for i in range(1, m + 1):
            if self.isSafe(node, color, graph, i):
                color[node] = i

                if self.solve(node + 1, color, m, N, graph):
                    return True

                color[node] = 0

        return False

    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        
        # Create adjacency list for the graph
        graph = [[0 , 0]] + [[] for _ in range(N)]

        for u, v in paths:
            graph[u].append(v)
            graph[v].append(u)
        
        print(graph)

        color = [0] * (N + 1)
        m = 4

        if self.solve(1, color, m, N, graph):
            return color[1:]
        else:
            return []