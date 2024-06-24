class Solution(object):
    def preorderTraversal(self, root):

        # def preorder(root , arr):

        #     if not root:
        #         return

        #     arr.append(root.val)
        #     preorder(root.left , arr)
        #     preorder(root.right , arr)

        #     return arr

        # return preorder(root , [])



        preorder = []
        
        if root is None:
            return preorder
        
        stack = []
        stack.append(root)
        
        while stack:

            root = stack.pop()

            preorder.append(root.val)

            if root.right:
                stack.append(root.right)

            if root.left:
                stack.append(root.left)

        return preorder