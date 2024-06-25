class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def backtrack(root, path):

            if not root:
                return False
            
            path.append(root.val)
            
            if not root.left and not root.right:
                if sum(path) == targetSum:
                    return True
            
            if backtrack(root.left, path): 
                return True

            if backtrack(root.right, path):
                return True

            path.pop()

            return False
        
        return backtrack(root, [])