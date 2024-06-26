class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def rec(root1 , root2):

            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False

            # Simultaneously we have to travserse the trees
            return root1.val == root2.val and rec(root1.left , root2.left) and rec(root1.right , root2.right)

        return rec(p , q)   