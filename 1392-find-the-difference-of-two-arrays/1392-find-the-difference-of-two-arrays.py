class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        l1 = []
        l2 = []
        l = []

        for i in range(len(nums1)):
            if(nums1[i] not in nums2):
                l1.append(nums1[i])
        
        for i in range(len(nums2)):
            if(nums2[i] not in nums1):
                l2.append(nums2[i])

        l.append(list(set(l1)))
        l.append(list(set(l2)))

        return l