class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        res = True
        
        root1 = root.left
        root2 = root.right

        def dfs(root1 , root2):

            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            return root1.val == root2.val and dfs(root1.left , root2.right) and dfs(root1.right , root2.left)
        
        return dfs(root1 , root2)