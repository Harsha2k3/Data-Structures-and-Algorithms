class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        j = -1

        for i in range(len(nums2)):
            nums1[j] = nums2[i]
            j -= 1

        nums1.sort()