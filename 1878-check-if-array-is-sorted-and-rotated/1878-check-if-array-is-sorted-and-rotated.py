class Solution:
    def check(self, nums: List[int]) -> bool:

        if sorted(nums) == nums:
            return True

        for i in range(1 , len(nums)):
            if nums[i] < nums[i - 1]:
                l1 = nums[:i]
                print(l1)
                l2 = nums[i:]
                print(l2)
                break
        
        return sorted(l2 + l1) == l2 + l1