class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        res = True

        def dfs(root):

            nonlocal res

            if not root:
                return 0

            lh = dfs(root.left)
            rh = dfs(root.right)

            res &= (abs(rh - lh) <= 1)

            return 1 + max(lh , rh)
        
        dfs(root)
        
        return res