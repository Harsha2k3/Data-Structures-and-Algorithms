class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        fm = float("inf")

        def find_fm(root):

            nonlocal fm

            if not root:
                return

            fm = min(fm , root.val)
            find_fm(root.left)
            find_fm(root.right)
        
        find_fm(root)

        sm = float("inf")

        def find_sm(root):

            nonlocal sm

            if not root:
                return

            if root.val > fm:
                sm = min(sm , root.val)

            find_sm(root.left)
            find_sm(root.right)
        
        find_sm(root)

        return sm if sm != float("inf") else -1