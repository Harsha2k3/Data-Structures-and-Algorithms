class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(root , l):

            nonlocal res

            if not root:
                return

            l.append(root.val)

            if not root.left and not root.right:
                res += int("".join(map(str , l)) , 2)

            dfs(root.left , l)
            dfs(root.right , l)
            
            l.pop()

        dfs(root , [])

        return res