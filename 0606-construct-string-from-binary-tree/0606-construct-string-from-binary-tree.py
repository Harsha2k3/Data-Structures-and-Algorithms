class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        result = str(root.val)
        
        if root.left or root.right:
            result += "(" + self.tree2str(root.left) + ")"
        
        if root.right:
            result += "(" + self.tree2str(root.right) + ")"
        
        return result