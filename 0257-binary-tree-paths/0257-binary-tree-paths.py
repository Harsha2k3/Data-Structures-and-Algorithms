class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        res = []

        def dfs(root , l):

            nonlocal res

            if not root.left and not root.right:
                res.append("".join(l) + str(root.val))
                return

            l.append(str(root.val) + '->')
            if root.left : dfs(root.left , l)
            if root.right : dfs(root.right , l)
            l.pop()

        dfs(root , [])
        
        return res