class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []

        def dfs(root):

            nonlocal res

            if not root:
                return
            
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        
        return res