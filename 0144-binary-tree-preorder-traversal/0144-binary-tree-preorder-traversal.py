# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):

        def preorder(root , arr):

            if not root:
                return

            arr.append(root.val)
            preorder(root.left , arr)
            preorder(root.right , arr)

            return arr

        return preorder(root , [])