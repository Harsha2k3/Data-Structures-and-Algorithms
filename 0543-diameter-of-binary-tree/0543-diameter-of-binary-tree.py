class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Diameter ==> Longest path between any 2 nodes
        # Same as 104. Maximum Depth of B.T with some changes
        # Just while checking height keep a track of lh + rh
        # At every node we can get lh and rh
        # We keep a track of the distance between
        # left most node of lst and right most node of rst of a node


        lp = 0

        def dfs(root):

            nonlocal lp

            if not root:
                return 0
            
            lh = dfs(root.left)
            rh = dfs(root.right)

            lp = max(lp , lh + rh)

            return 1 + max(lh , rh)
        
        dfs(root)
        
        return lp