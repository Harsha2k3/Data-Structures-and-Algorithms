from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        res = []

        q = deque()

        q.append(root)

        while q:

            l = []

            for i in range(len(q)):

                node = q.popleft()

                if node: l.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            res.append(l)

        return res