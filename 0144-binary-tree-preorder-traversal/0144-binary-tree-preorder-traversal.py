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


        # # (Or)


        # preorder = []
        
        # if root is None:
        #     return preorder
        
        # stack = []
        # stack.append(root)
        
        # while stack:

        #     root = stack.pop()

        #     preorder.append(root.val)

        #     if root.right:
        #         stack.append(root.right)

        #     if root.left:
        #         stack.append(root.left)

        # return preorder



        # Same as Morris Inorder 
        # Just keep preorder.append(curr.val) in "if not prev.right:"
        # Because, as it's root-left-right we have to take
        # the node when we are making the connection



        preorder = []

        curr = root

        while curr:

            if not curr.left:
                preorder.append(curr.val)
                curr = curr.right

            else:

                prev = curr.left

                while(prev.right and prev.right != curr):
                    prev = prev.right
                
                if not prev.right:
                    prev.right = curr
                    preorder.append(curr.val)
                    curr = curr.left

                else:
                    prev.right = None
                    curr = curr.right
        
        return preorder