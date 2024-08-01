class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(root):

            nonlocal res

            if not root:
                return

            if not root.left and not root.right:
                return root.val

            if dfs(root.left):
                res += dfs(root.left)
            dfs(root.right)

        dfs(root)

        return res