class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) != len(postorder):
            return None

        hm = {val : i for i , val in enumerate(inorder)}

        return self.buildTreePostIn(inorder , 0 , len(inorder) - 1 , postorder , 0 , len(postorder) - 1 , hm)

    def buildTreePostIn(self, inorder: List[int], is_, ie, postorder: List[int], ps, pe, hm):

        # is ==> Inorder start
        # ie ==> Inorder end
        # ps ==> Postorder start
        # pe ==> Postorder end

        if ps > pe or is_ > ie:
            return None

        root = TreeNode(postorder[pe])

        inRoot = hm[postorder[pe]]

        numsLeft = inRoot - is_

        root.left = self.buildTreePostIn(inorder , is_ , inRoot - 1 , postorder , ps , ps + numsLeft - 1 , hm)

        root.right = self.buildTreePostIn(inorder , inRoot + 1 , ie , postorder , ps + numsLeft , pe - 1 , hm)

        return root        