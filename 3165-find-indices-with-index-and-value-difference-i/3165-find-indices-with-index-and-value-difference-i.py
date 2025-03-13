class Solution:
    def findIndices(self, nums: List[int], id: int, vd: int) -> List[int]:

        l , r = 0 , 0

        while r < len(nums):

            if abs(l - r) >= id and abs(nums[l] - nums[r]) >= vd:
                return [l , r]
            
            r += 1

            if r == len(nums) and l < len(nums) - 1:
                l += 1
                r = l       

        return [-1 , -1]