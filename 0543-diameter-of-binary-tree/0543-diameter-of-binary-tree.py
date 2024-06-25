class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        lp = 0

        def rec(root):

            nonlocal lp

            if not root:
                return 0

            lh = rec(root.left)
            rh = rec(root.right)

            lp = max(lp , lh + rh)

            return 1 + max(lh, rh)

        rec(root)

        return lp