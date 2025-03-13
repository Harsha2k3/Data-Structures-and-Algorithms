class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        # # S.C = O(n)

        # if(k > len(nums)):
        #     k = k - len(nums)
        
        # t = nums[0:len(nums)-k]

        # nums[0:len(nums)-k] = nums[len(nums)-k:]
        # nums[len(nums)-k:] = t

        # return nums


        # S.C = O(1)

        # Wacth from 4:35 to 6:30
        # https://www.youtube.com/watch?v=BHr381Guz3Y

        # Reversing entire array
        l , r = 0 , len(nums) - 1

        while l < r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1

        # Reversing the array from 0 to k - 1
        k = k % len(nums)
        l , r = 0 , k - 1

        while l < r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1
        
        # Reversing the array from k to len(nums) - 1
        l , r = k , len(nums) - 1

        while l < r:
            nums[l] , nums[r] = nums[r] , nums[l]
            l += 1
            r -= 1

        return nums