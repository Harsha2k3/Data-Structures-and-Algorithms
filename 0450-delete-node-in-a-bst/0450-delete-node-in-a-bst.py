class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        res = root

        if not root:
            return root
        
        if root.val == key:
            return self.helper(root)

        while root:

            if key < root.val:
                if root.left and key == root.left.val:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            
            else:
                if root.right and key == root.right.val:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right

        return res

    def helper(self , root):

        if not root.left:
            return root.right
        
        if not root.right:
            return root.left

        rightChild = root.right
        lastRight = self.find_lr(root.left)
        lastRight.right = rightChild
        return root.left
    
    def find_lr(self , root):
        if not root.right:
            return root
        return self.find_lr(root.right)