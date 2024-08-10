class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        maxDepth = 0

        def dfs(root , cd):
            
            nonlocal res , maxDepth

            if not root:
                return

            if cd > maxDepth:
                res = root.val
                maxDepth = cd

            dfs(root.left , cd + 1)    
            dfs(root.right , cd + 1)
        
        dfs(root , 1)    # cd ==> Current Depth
        
        return res