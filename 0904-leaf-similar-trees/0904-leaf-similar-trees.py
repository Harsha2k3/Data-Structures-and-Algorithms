class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(root , l):

            if not root:
                return

            if root and not root.left and not root.right:
                l.append(root.val)

            dfs(root.left , l)
            dfs(root.right , l)

            return l

        return dfs(root1 , []) == dfs(root2 , [])