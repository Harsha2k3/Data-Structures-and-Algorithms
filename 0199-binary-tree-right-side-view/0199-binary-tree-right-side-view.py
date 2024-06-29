from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        q = deque()

        if not root:
            return res

        q.append(root)

        while q:

            f = 0

            for i in range(len(q)):

                node = q.popleft()

                if f == 0:   
                    # We use a flag, just to grab the 1st node in each level
                    f = 1
                    res.append(node.val)
                
                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)
        
        return res