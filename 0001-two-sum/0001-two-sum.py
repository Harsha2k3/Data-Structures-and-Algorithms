class Solution(object):
    def twoSum(self, nums, t):

        l = []
        k = 1

        for i in range(len(nums)):
            for j in range(k,len(nums)):
                if(nums[i]+nums[j] == t):
                    l.append(i)
                    l.append(j)
                    break
            k+=1
        
        return l