class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Mix of both 104. Maximum Depth of Binary Tree
        # and 543. Diameter of Binary Tree

        mps = float("-inf")

        def dfs(root):

            nonlocal mps

            if not root:
                return 0
            
            mls = max(0 , dfs(root.left))
            mrs = max(0 , dfs(root.right))

            mps = max(mps , mls + root.val + mrs)

            return root.val + max(mls , mrs)

        dfs(root)

        return mps