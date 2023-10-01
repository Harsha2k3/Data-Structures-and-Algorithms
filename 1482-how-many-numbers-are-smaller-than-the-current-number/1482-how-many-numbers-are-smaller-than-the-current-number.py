class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        count = []
        c = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if(nums[j]<nums[i]):
                    c += 1
            count.append(c)
            c = 0
        
        return count