class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        res = 0

        def dfs(root):

            nonlocal res

            if not root:
                return

            dfs(root.left)
            dfs(root.right)

            if low <= root.val <= high:
                res += root.val 

            return res

        return dfs(root)