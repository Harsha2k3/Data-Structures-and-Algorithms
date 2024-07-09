class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        while True:

            if not root:
                return None

            if root.val == val:
                return root

            if val < root.val:
                root = root.left

            else:
                root = root.right