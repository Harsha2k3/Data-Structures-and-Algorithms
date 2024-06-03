class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findStart(nums, target):
            start = -1
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    start = mid
                    right = mid - 1
                    # We will search towards left, to search if there is any much smaller element than current one
                    # As left side has a way smaller elements
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return start

        def findEnd(nums, target):
            end = -1
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    end = mid
                    left = mid + 1  
                    # We will search towards right, to search if there is any much smaller element than current one
                    # As right side has larger elements
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return end

        start = findStart(nums, target)
        end = findEnd(nums, target)

        if start != -1:
            return [start, end]
        else:
            return [-1, -1]


# class Solution:
#     def searchRange(self, array: List[int], val: int) -> List[int]:

#         start = 0
#         end = len(array) - 1

#         l = []
#         p = 0

#         mid = (start + end) // 2
        
#         while(start <= end):
#             if(val < array[mid]):
#                 end = mid - 1
#             else:
#                 start = mid + 1
            
#             mid = (start + end) // 2

#             if(array[mid] == val):
#                 l.append(array.index(array[mid]) + p)
#                 array.pop(mid)
#                 p += 1        # Number of pop's
                
#                 # Re-setting the pointers
#                 start = 0
#                 end = len(array) - 1
#                 mid = (start + end) // 2
                
            
#         return [-1,-1] if l == [] else [min(l),max(l)]

# This works fine, but takes extra complexity due to l.append(array.index(array[mid]) + p), as this line takes O(n)

# It's better to work with the indices obtained during the binary search directly.

# Time Complexity: O(log n) - Binary search is used twice to find the starting and ending positions.
# Space Complexity: O(1) - Constant extra space is used to store variables, and no additional data structures are used.