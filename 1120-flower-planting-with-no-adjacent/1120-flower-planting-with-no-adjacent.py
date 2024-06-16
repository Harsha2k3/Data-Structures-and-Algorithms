class Solution:

    # Same as m - coloring problem in backtracking

    def isSafe(self, node, color, graph, col):

        for neighbor in graph[node]:
            if color[neighbor] == col:
                return False
        return True

    def solve(self, node, color, m, N, graph):

        if node == N:
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
        graph = [[] for _ in range(N)]

        for u, v in paths:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)

        color = [0] * N
        m = 4

        if self.solve(0, color, m, N, graph):
            return color
        else:
            return []