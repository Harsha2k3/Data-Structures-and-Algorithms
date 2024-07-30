class Solution:
    def getTargetCopy(self, root1: TreeNode, root2: TreeNode, target: TreeNode) -> TreeNode:

        res = None 

        def dfs(root1 , root2):

            nonlocal res

            if not root1:
                return

            if root1 == target:
                res = root2
                return

            dfs(root1.left , root2.left)
            dfs(root1.right , root2.right)
            
        dfs(root1 , root2)

        return res