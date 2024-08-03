class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        res = 0

        def dfs(root , count):

            nonlocal res

            if not root:
                return 0 , 0    # sum , count
                
            ls , lc = dfs(root.left , count)
            rs , rc = dfs(root.right , count)

            curr_count = 1 + lc + rc

            if root.val == (root.val + ls + rs) // curr_count:
                res += 1
            
            return root.val + ls + rs , curr_count

        dfs(root , 0)

        return res