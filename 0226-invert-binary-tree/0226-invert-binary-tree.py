class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Apply BFS and swap left and right children at every node

        queue = [root]

        while queue:

            curr = queue.pop(0)

            if not curr:
                continue

            curr.left , curr.right = curr.right ,curr.left

            queue.append(curr.left)
            queue.append(curr.right)
            
        return root