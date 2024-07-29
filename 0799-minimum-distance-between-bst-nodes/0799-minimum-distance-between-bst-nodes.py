class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

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