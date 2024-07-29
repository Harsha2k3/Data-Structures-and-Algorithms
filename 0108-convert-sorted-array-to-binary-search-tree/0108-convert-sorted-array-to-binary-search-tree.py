# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dfs(l):

            if not l:
                return

            mid = len(l) // 2

            root = TreeNode(l[mid] , None , None)
            root.left = dfs(l[:mid])
            root.right = dfs(l[mid + 1 :])

            return root
        
        return dfs(nums)