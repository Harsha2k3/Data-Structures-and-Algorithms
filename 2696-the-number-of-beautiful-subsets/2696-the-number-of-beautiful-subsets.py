class Solution(object):
    def beautifulSubsets(self, nums, k):

        def rec(i, subset, count):

            if i == len(nums):
                return 1 if subset else 0
            
            # Don't include nums[i] in the subset
            res = rec(i + 1, subset, count)
            
            # Include nums[i] in the subset if it forms a beautiful subset
            if not count[nums[i] + k] and not count[nums[i] - k]:
                subset.append(nums[i])
                count[nums[i]] += 1
                res += rec(i + 1, subset, count)
                subset.pop() 
                count[nums[i]] -= 1
            
            return res

        return rec(0, [], defaultdict(int))