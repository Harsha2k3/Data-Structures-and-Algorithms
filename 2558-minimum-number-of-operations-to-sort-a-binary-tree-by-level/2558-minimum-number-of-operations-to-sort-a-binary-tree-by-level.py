from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        q = deque()

        q.append(root)
        
        def bfs():

            nonlocal res

            while q:
                level = []
                for i in range(len(q)):

                    node = q.popleft()
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

                sorted_level = sorted(level)

                swaps = 0

                for i in range(len(level)):
                    if level[i] != sorted_level[i]:
                        j = level.index(sorted_level[i])
                        level[i] , level[j] = level[j] , level[i]
                        swaps += 1
                
                res += swaps
        
        bfs()

        return res