class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        return root.left.val + root.right.val == root.val        