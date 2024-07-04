class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        # We follow right-left-root

        prev = None

        def rec(node):

            nonlocal prev

            if not node:
                return

            rec(node.right)
            rec(node.left)

            node.right = prev
            node.left = None
            prev = node

        rec(root)

        return root        