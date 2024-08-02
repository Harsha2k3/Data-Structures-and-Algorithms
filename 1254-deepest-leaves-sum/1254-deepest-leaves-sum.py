class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        maxd = float("-inf")   # Max depth
        res = 0

        def dfs(root , d):

            nonlocal  maxd , res

            if not root:
                return

            if not root.left and not root.right:
                
                if d > maxd:
                    maxd = d
                    res = root.val

                elif d == maxd:
                    res += root.val

                return

            dfs(root.left , d + 1)
            dfs(root.right , d + 1)

        dfs(root , 1)

        return res