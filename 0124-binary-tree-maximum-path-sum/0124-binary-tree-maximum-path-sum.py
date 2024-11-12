class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Mix of both 104. Maximum Depth of Binary Tree
        # and 543. Diameter of Binary Tree

        mps = float("-inf")     # Max path sum

        def rec(root):

            nonlocal mps

            if not root:
                return 0

            mls = max(0 , rec(root.left))     # Max left sum
            mrs = max(0 , rec(root.right))    # Max right sum

            # Here we do mls = max(0 , rec(root.left)) and mrs = max(0 , rec(root.right))
            # not mls = max(mls , rec(root.left)) and mrs = max(mrs , rec(root.right))
            # Because we should not consider -ve values
            # https://www.youtube.com/watch?v=WszrfSwMz58&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=19
            # Watch from 13:24 to 14:41

            mps = max(mps , mls + root.val + mrs)

            return root.val + max(mls , mrs)

        rec(root)

        return mps