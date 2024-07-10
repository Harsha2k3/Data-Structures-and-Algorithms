class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def inorder(root , count_res):
        
            if not root:
                return

            inorder(root.left , count_res)

            count_res[0] += 1
            if count_res[0] == k:
                count_res[1] = root.val
                return

            inorder(root.right, count_res)

        # count = count_res[0] , res = count_res[1]
        count_res = [0 , -1000]  
        
        inorder(root , count_res)

        return count_res[1]