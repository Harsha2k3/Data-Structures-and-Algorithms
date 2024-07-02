class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()

        # [4,5,9]
        # [4,4,8,9,9]
        
        # [1,1,2,2]
        # [2,2]

        i  , j = 0 , 0

        res = []

        while i <= len(nums1) - 1 and j <= len(nums2) - 1:

            if nums1[i] == nums2[j]:
                res.append(nums1[i])
                i += 1
                j += 1

            elif nums1[i] > nums2[j]:
                j += 1

            elif nums1[i] < nums2[j]:
                i += 1

        return res