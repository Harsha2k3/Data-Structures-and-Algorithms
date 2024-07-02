class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def count(root):

            if not root:
                return 0

            lh = leftheight(root)
            rh = rightheight(root)

            if lh == rh:
                return (2 ** lh) - 1

            return 1 + count(root.left) + count(root.right)

        def leftheight(root):

            h = 0

            while root:
                h += 1
                root = root.left
            return h

        def rightheight(root):

            h = 0

            while root:
                h += 1
                root = root.right
            return h
        
        return count(root)