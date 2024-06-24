class Solution(object):
    def postorderTraversal(self, root):

        def postorder(root , arr):

            if not root:
                return

            postorder(root.left , arr)
            postorder(root.right , arr)
            arr.append(root.val)

            return arr

        return postorder(root , [])