class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        
        if not root:
            return res
        
        q = deque()

        q.append(root)

        leftToRight = True

        while q:

            size = len(q)

            level = [0] * size

            for i in range(size):

                node = q.popleft()

                index = i if leftToRight else (size - i - 1)
                
                level[index] = node.val             

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
            

            leftToRight = not leftToRight
            
            res.append(level)
        
        return res