from collections import deque

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        q = deque()

        q.append(root)

        res = []

        if not root:
            return []

        while q:

            s = 0
            c = 0

            for i in range(len(q)):

                node = q.popleft()

                s += node.val
                c += 1

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            
            res.append(s / c)

        return res