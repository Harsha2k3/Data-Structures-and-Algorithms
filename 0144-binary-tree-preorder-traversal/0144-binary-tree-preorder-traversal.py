class Solution(object):
    def preorderTraversal(self, root):

        def preorder(root , arr):

            if not root:
                return

            arr.append(root.val)
            preorder(root.left , arr)
            preorder(root.right , arr)

            return arr

        return preorder(root , [])