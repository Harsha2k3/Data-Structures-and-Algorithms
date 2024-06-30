class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.groups = n - 1
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        x = self.find(i)
        y = self.find(j)
        if x == y:
            return False
        else:
            self.parent[y] = x
            self.groups -= 1
            return True


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        alice = UnionFind(n)
        bob = UnionFind(n)
        count = 0
        
        for edge in edges:
            type, u, v = edge[0], edge[1] - 1, edge[2] - 1
            if type == 3 and alice.union(u, v) and bob.union(u, v):
                count += 1
        
        for edge in edges:
            type, u, v = edge[0], edge[1] - 1, edge[2] - 1
            if (type == 1 and alice.union(u, v)) or (type == 2 and bob.union(u, v)):
                count += 1
        
        if alice.groups == 0 and bob.groups == 0:
            return len(edges) - count
        else:
            return -1