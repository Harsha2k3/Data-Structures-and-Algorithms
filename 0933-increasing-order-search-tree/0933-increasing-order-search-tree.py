class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        prev = None
        new_root = None

        def inorder(root):

            nonlocal prev , new_root

            if not root:
                return 

            inorder(root.left)

            if prev:
                prev.right = root

            else:
                new_root = root

            root.left = None
            prev = root

            inorder(root.right)

            return new_root
        
        return inorder(root)