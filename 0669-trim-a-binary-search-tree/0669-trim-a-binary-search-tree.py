class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        if not root: 
            return None
            
        root.left = self.trimBST(root.left , low , high)
        root.right = self.trimBST(root.right , low , high)    
        
        if(low <= root.val <= high):
            return root
            
        if root.left:
            return root.left
            
        else:
            return root.right