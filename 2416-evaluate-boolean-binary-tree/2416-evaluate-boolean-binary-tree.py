class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):

            if not root:
                return

            if not root.left and not root.right:

                if root.val == 1:
                    return True

                else:
                    return False

            l = dfs(root.left)
            r = dfs(root.right)

            if root.val == 2:
                return l or r

            if root.val == 3:
                return l and r

        return dfs(root)