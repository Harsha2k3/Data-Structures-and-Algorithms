from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        q = deque()

        if not root:
            return res

        q.append(root)

        while q:

            k = 0

            for i in range(len(q)):

                node = q.popleft()

                if k == 0:
                    k = 1
                    res.append(node.val)
                
                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)

            # res.append(level[-1])
        
        return res