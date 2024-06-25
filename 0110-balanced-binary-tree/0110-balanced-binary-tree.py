class Solution(object):
    def isBalanced(self, root):

        def check(root):

            if not root:
                return 0

            lh = check(root.left)

            if lh == -1:
                return -1

            rh = check(root.right)

            if rh == -1:
                return -1

            if abs(lh - rh) > 1:
                return -1

            return 1 + max(lh , rh)

        return check(root) != -1