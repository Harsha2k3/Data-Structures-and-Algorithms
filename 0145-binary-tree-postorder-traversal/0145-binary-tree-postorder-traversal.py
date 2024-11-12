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

        # def postorder(root , arr):

        #     if not root:
        #         return

        #     postorder(root.left , arr)
        #     postorder(root.right , arr)
        #     arr.append(root.val)

        #     return arr

        # return postorder(root , [])

        # # (Or)

        # # Using 2 stacks

        # postorder = []

        # if root is None:
        #     return postorder

        # st1, st2 = [], []

        # st1.append(root)

        # while st1:

        #     root = st1.pop()

        #     st2.append(root)

        #     if root.left is not None:
        #         st1.append(root.left)

        #     if root.right is not None:
        #         st1.append(root.right)

        # while st2:
        #     postorder.append(st2[-1].val)
        #     st2.pop()

        # return postorder


        # # (Or)

        # Using 1 stack

        curr = root

        stack = []

        postorder = []

        while curr or stack:

            if curr:
                stack.append(curr)
                curr = curr.left
            
            else:
                temp = stack[-1].right

                if not temp:
                    temp = stack[-1]
                    stack.pop()
                    postorder.append(temp.val)

                    while stack and temp == stack[-1].right:
                        temp = stack[-1]
                        stack.pop()
                        postorder.append(temp.val)

                else:
                    curr = temp

        return postorder