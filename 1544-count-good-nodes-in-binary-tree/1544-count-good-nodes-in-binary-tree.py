class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        def dfs(root , m):

            nonlocal res

            if not root:
                return

            if root.val >= m:
                res += 1

            m = max(m , root.val)

            dfs(root.left , m)
            dfs(root.right , m)

        dfs(root , -100000)

        return res