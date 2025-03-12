class Solution(object):
    def twoSum(self, nums, t):

        d = {}

        # Store indices as lists to handle duplicates
        for i , num in enumerate(nums):
            if num in d:
                d[num].append(i)
            else:
                d[num] = [i]

        nums.sort()

        l , r = 0 , len(nums) - 1

        while l < r:
            if nums[l] + nums[r] == t:
                return [d[nums[l]].pop(0) , d[nums[r]].pop(0)]
            
            elif nums[l] + nums[r] > t:
                r -= 1
            
            else:
                l += 1