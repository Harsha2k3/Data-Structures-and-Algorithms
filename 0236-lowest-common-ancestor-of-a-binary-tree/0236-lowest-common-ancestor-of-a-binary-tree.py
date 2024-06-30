class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left , p , q)
        r = self.lowestCommonAncestor(root.right , p , q)

        if not l:
            return r
        
        elif not r:
            return l

        else:
            return root