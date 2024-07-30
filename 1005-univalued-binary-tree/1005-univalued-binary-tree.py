class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        val = root.val

        res = True

        def dfs(root):

            nonlocal res

            if not root:
                return

            if root.val != val:
                res = res and False

            dfs(root.left)
            dfs(root.right)

        dfs(root)

        return res