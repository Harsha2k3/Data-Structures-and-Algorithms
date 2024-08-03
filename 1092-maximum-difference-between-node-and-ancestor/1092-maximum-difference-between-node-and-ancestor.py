class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(root , max_ , min_):

            nonlocal res  

            if not root:
                return

            max_ = max(max_ , root.val)
            min_ = min(min_ , root.val)

            res = max(res , abs(max_ - min_))

            dfs(root.left , max_ , min_)
            dfs(root.right ,  max_ , min_)

        dfs(root , root.val , root.val)

        return res