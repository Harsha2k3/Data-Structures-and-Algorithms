class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        count = 0
        j = 0
        l = []
        k = -1

        for i in range(len(nums)):
            if(nums[i] == 0):
                l.append(nums[i])
                count += 1
            else:
                nums[j] = nums[i]
                j += 1

        for i in range(count):
            nums.pop(k)

        for i in range(count):
            nums.append(0)