class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        prev = [float("-inf")]  
        b = [True]
        res = [True]
        
        def inorder(root):

            if not root:
                return

            inorder(root.left)

            if root.val <= prev[0]:
                res[0] = False
                b[0] = b[0] and res[0]
            
            prev[0] = root.val
            
            inorder(root.right)

        inorder(root)

        return b[0]