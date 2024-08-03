class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:

        res = 0

        def dfs(root):

            nonlocal res

            if not root:
                return

            if root.val % 2 == 0:
                if root and root.left and root.left.left:
                    res += root.left.left.val
                if root and root.left and root.left.right:
                    res += root.left.right.val
                if root and root.right and root.right.left:
                    res += root.right.left.val
                if root and root.right and root.right.right:
                    res += root.right.right.val

            dfs(root.left)
            
            dfs(root.right)
        
        dfs(root)

        return res