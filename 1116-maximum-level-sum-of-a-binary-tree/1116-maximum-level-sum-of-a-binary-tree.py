from collections import deque

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

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

        fres = -1000000000000000000

        for i in res:
            fres = max(fres , sum(i))

        for i in range(len(res)):
            if sum(res[i]) == fres:
                return i + 1