class Solution(object):
    def diameterOfBinaryTree(self, root):
        def rec(root, lp):
            if not root:
                return 0

            lh = rec(root.left, lp)
            rh = rec(root.right, lp)

            lp[0] = max(lp[0], lh + rh)

            return 1 + max(lh, rh)

        lp = [0]  
        rec(root, lp)

        return lp[0]
