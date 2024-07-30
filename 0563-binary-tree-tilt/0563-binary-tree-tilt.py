class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(root):

            nonlocal res

            if not root:
                return 0
            
            left_sum = dfs(root.left)
            right_sum = dfs(root.right)
            
            res += abs(left_sum - right_sum)
            
            return left_sum + right_sum + root.val
        
        dfs(root)

        return res