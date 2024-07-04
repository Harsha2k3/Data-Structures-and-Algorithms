class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

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