class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def inorder(root):

            if not root:
                return []

            return inorder(root.left) + [root.val] + inorder(root.right)
        
        l1 = inorder(root1)
        l2 = inorder(root2)
        
        res = []
        i , j = 0 , 0
        
        while i < len(l1) and j < len(l2):

            if l1[i] < l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1
        
        while i < len(l1):
            res.append(l1[i])
            i += 1
        
        while j < len(l2):
            res.append(l2[j])
            j += 1
        
        return res