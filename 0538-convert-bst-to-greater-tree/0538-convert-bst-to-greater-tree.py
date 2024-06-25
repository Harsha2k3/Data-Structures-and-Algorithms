class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.value = 0
        
        def dfs(node):
            
            if not node:
                return
            
            dfs(node.right)
            self.value += node.val
            node.val = self.value
            dfs(node.left)
        
        dfs(root)

        return root        