class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        
        res = None

        def dfs(root , path):
            
            nonlocal res

            if not root:
                return

            path.append(chr(root.val + ord('a')))

            if not root.left and not root.right:
                rev_path = "".join(path[::-1])
                if not res or rev_path < res:
                    res = rev_path

            dfs(root.left , path)
            dfs(root.right , path)
            path.pop()

        dfs(root , [])

        return res