class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        if(k == 1):
            return nums

        queue = []
        res = []
        
        i = 0
        j = 0
        count = 0
        
        while i < len(nums) - k + 1:
            count += 1
            
            if not queue:
                queue.append(nums[j])
                
            elif queue and queue[-1] >= nums[j]:
                queue.append(nums[j])
            else:
                while queue and queue[-1] < nums[j]:
                    queue.pop()
                queue.append(nums[j])
            
            if count == k:
                res.append(queue[0])
                if nums[i] == queue[0]:
                    queue.pop(0)
                count -= 1
                i += 1
            j += 1

        return res