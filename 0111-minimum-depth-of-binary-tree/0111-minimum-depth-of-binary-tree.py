class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        mind = float("inf")

        def dfs(root , d):

            nonlocal mind

            if not root:
                return
            
            if not root.left and not root.right:
                mind = min(mind , d)
                return

            dfs(root.left , d + 1)
            dfs(root.right , d + 1)

        dfs(root , 1)

        return mind