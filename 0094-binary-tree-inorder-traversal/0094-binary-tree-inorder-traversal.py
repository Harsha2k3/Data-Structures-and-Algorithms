class Solution(object):
    def inorderTraversal(self, root):

        if not root:
            return []

        def inorder(root , arr):

            if not root:
                return

            inorder(root.left , arr)
            arr.append(root.val)
            inorder(root.right , arr)

            return arr
        
        return inorder(root , [])



        # inorder = []

        # if not root:
        #     return inorder

        # stack = []

        # while root or stack:

        #     # At every node go to left most node
        #     while root:              
        #         stack.append(root)
        #         root = root.left

        #     root = stack.pop()
        #     inorder.append(root.val)
        #     root = root.right

        # return inorder





        # Inorder using Recrsion ==> O(n) auxiliary space
        # Inorder using Stack    ==> O(n) space for stack
        # Morris Inorder         ==> O(1) space
        # Every time we go to left subtree of current and then we will go to it's complete right
        # Once we reach right node of the left subtree,
        # We will make (that node).right = current node
        # So that we can go to the current node i.e, 
        # We can go to the root of that sub-tree directly
        # without backtracking
        # While we visit (that node) again make sure we 
        # that the connection is removed
        # So, (that node).right = None
        
        # https://leetcode.com/problems/binary-tree-inorder-traversal/solutions/5415690/morris-inorder-o-1-space/
        # See Picture here (Threaded binary tree)
        # We make use of the connections that are created 
        # to directly go to the root nodes of a subtree instead
        # of backtracking 
        # And we remove the threads (Connections)


        inorder = []

        curr = root

        while curr:

            if not curr.left:
                inorder.append(curr.val)
                curr = curr.right

            else:

                prev = curr.left

                while(prev.right and prev.right != curr):
                    prev = prev.right
                
                if not prev.right:
                    prev.right = curr
                    curr = curr.left

                else:
                    prev.right = None
                    inorder.append(curr.val)
                    curr = curr.right
        
        return inorder