class Solution(object):
    def postorderTraversal(self, root):

        # def postorder(root , arr):

        #     if not root:
        #         return

        #     postorder(root.left , arr)
        #     postorder(root.right , arr)
        #     arr.append(root.val)

        #     return arr

        # return postorder(root , [])

        # # (Or)

        postorder = []

        if root is None:
            return postorder

        st1, st2 = [], []

        st1.append(root)

        while st1:

            root = st1.pop()

            st2.append(root)

            if root.left is not None:
                st1.append(root.left)

            if root.right is not None:
                st1.append(root.right)

        while st2:
            postorder.append(st2[-1].val)
            st2.pop()

        return postorder