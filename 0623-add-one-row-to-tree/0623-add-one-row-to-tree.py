class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
    
        def dfs(root , d):
            
            if not root:
                return

            if d == depth - 1:
                oldLeft = root.left
                oldRight = root.right
                root.left = TreeNode(val)
                root.right = TreeNode(val)
                root.left.left = oldLeft
                root.right.right = oldRight
                
                return
                
            else:
                dfs(root.left , d + 1)
                dfs(root.right , d + 1)
        
        dfs(root , 1)

        return root