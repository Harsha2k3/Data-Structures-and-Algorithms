class Solution:
    def search(self, nums: List[int], val: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == val:
                return mid
            
            elif nums[mid] > val:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return -1