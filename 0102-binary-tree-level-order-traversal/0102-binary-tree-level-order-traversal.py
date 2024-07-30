from collections import deque

class Solution(object):
    def levelOrder(self, root):

        res = []

        q = deque()

        if not root:
            return res

        q.append(root)

        j = 0

        while q:

            level = []

            for i in range(len(q)):

                node = q.popleft()

                level.append(node.val)

                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)

            res.append(level)
        
        return res