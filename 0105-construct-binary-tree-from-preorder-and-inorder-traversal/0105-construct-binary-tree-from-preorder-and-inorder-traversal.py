class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # https://www.youtube.com/watch?v=aZNaLrVebKQ&list=PLkjdNRgDmcc0Pom5erUBU4ZayeU9AyRRu&index=35
        # Watch from 2:35 to 6:44

        inMap = {val : idx for idx , val in enumerate(inorder)}

        root = self._buildTree(preorder , 0 , len(preorder) - 1 , inorder , 0 , len(inorder) - 1 , inMap)
        
        return root

    def _buildTree(self , preorder , preStart , preEnd , inorder , inStart , inEnd , inMap):
       
        if preStart > preEnd or inStart > inEnd:
            return None

        root = TreeNode(preorder[preStart])

        inRoot = inMap[root.val]

        numsLeft = inRoot - inStart

        root.left = self._buildTree(preorder , preStart + 1 , preStart + numsLeft , inorder , inStart , inRoot - 1 , inMap)

        root.right = self._buildTree(preorder , preStart + numsLeft + 1 , preEnd , inorder , inRoot + 1 , inEnd , inMap)

        return root