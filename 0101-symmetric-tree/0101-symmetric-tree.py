class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        root1 , root2 = root.left , root.right

        def rec(root1 , root2):

            if (not root1) or (not root2):
                return root1 == root2

            if root1.val != root2.val:
                return False

            # root1 , root2 = root1.left , root2.right

            # if rec(root1 , root2):
            #     return True
            # return False

            # # Backtracking
            # root1 , root2 = root1.right , root2.left

            # if rec(root1 , root2):
            #     return True
            # return False

            return rec(root1.left , root2.right) and rec(root1.right , root2.left)

        return not root or rec(root1 , root2)