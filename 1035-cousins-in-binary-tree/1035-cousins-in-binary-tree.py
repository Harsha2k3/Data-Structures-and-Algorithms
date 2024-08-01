class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        pm = {}

        def getParent(root , parent):

            nonlocal pm

            if not root:
                return
            
            pm[root.val] = parent
            getParent(root.left, root)
            getParent(root.right, root)

        getParent(root , None)
        
        x_depth = y_depth = 0

        def dfs(root , depth):

            nonlocal x_depth , y_depth

            if not root:
                return

            if root.val == x:
                x_depth = depth

            if root.val == y:
                y_depth = depth

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)


        dfs(root, 0)
        
        return x_depth == y_depth and pm[x] != pm[y]