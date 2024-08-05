class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:

        def dfs(root , parent , is_left):

            if not root:
                return
            
            dfs(root.left , root , True)
            dfs(root.right , root , False)
            
            if not root.left and not root.right and root.val == target:
                if parent:
                    if is_left:
                        parent.left = None
                    else:
                        parent.right = None

        dfs(root, None, False)

        if root and not root.left and not root.right and root.val == target:
            return None
        
        return root