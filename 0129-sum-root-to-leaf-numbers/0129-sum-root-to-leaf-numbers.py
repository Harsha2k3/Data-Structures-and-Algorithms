class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        l = []
        res = 0

        def dfs(root):

            nonlocal l , res
            
            if not root.left and not root.right:
                l.append(str(root.val))
                res += int("".join(l))
                return

            l.append(str(root.val))
            if root.left:
                dfs(root.left)
                l.pop()
            if root.right:
                dfs(root.right)
                l.pop()
        
        dfs(root)

        return res