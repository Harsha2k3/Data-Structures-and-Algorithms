class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # Consider a sorted array, [1 , 2 , 3 , 4]
        # As it is sorted to find min difference between 2 items
        # we can just find difference between adjacent elements
        # i.e, 2 - 1 , 3 - 2 , 4 - 3
        # Inorder traversal of a BST is a sorted array
        # So apply the same here by doing an inorder traversal
        # by tracking prev node and current node

        prev = None
        res = float("inf")
        
        def inorder(root):

            nonlocal prev , res

            if not root:
                return

            inorder(root.left)

            if prev:
                res = min(res , root.val - prev.val)
                
            
            prev = root

            inorder(root.right)

        inorder(root)
        
        return res        