class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        lh , rh = 0 , 0

        def dfs(root):

            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)

            return 1 + max(lh , rh)
        
        return dfs(root)