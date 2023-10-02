class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        s = set(nums)
        count = 0

        for i in s:
            if(nums.count(i) <= 2):
                for j in range(nums.count(i)):
                    nums.append(i)
                    count += 1
            elif(nums.count(i) > 2):
                for k in range(2):
                    nums.append(i)
                    count += 1
        
        j = (-1*count)-1

        for i in range(len(nums)-count):
            nums.pop(j)
        
        nums.sort()