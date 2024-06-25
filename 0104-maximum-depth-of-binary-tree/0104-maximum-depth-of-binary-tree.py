class Solution(object):
    def maxDepth(self, root):

        def rec(root):

            if not root:
                return 0

            lh = rec(root.left)
            rh = rec(root.right)

            return 1 + max(lh , rh)

        return rec(root)