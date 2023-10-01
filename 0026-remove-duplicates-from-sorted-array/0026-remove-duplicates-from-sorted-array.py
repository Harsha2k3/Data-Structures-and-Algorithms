class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        s = set(nums)
        l = []
        count = 0

        for i in s:
            nums.append(i)
            count += 1
        
        j = (-1*count)-1

        for i in range(len(nums)-count):
            nums.pop(j)
        
        nums.sort()