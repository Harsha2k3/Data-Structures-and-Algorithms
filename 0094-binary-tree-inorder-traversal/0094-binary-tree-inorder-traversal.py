class Solution(object):
    def inorderTraversal(self, root):

        def inorder(root , arr):

            if not root:
                return

            inorder(root.left , arr)
            arr.append(root.val)
            inorder(root.right , arr)

            return arr

        return inorder(root , [])