class Solution:
    def amountOfTime(self, root: Optional[TreeNode], t: int) -> int:

        pm = defaultdict(int)  # Parent Map

        visited = set()

        max_time = 0

        target = None

        def getParent(root , parent , t):

            nonlocal target
            
            if not root:
                return

            if root.val == t:
                target = root

            pm[root] = parent
            getParent(root.left , root, t)
            getParent(root.right , root, t)

        def dfs(node , time):
            
            nonlocal max_time
            
            if not node or node in visited:
                return

            visited.add(node)
            
            max_time = max(max_time , time)
            
            dfs(node.left , time + 1)
            dfs(node.right , time + 1)
            dfs(pm[node] , time + 1)

        getParent(root , None , t)
        
        if target:
            dfs(target , 0)

        return max_time        