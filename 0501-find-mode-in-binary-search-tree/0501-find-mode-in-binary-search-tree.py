class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
                    
        current_val = None
        current_count = 0
        max_count = 0
        modes = []

        def inorder(root):

            nonlocal current_val , current_count , max_count , modes
            
            if not root:
                return
            
            inorder(root.left)
            
            current_count = current_count + 1 if root.val == current_val else 1
            current_val = root.val
            
            if current_count > max_count:
                max_count = current_count
                modes = [current_val]
            
            elif current_count == max_count:
                modes.append(current_val)
            
            inorder(root.right)

        inorder(root)

        return modes