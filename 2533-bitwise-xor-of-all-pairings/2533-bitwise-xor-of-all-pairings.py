class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        # Answer is (2^10)^(2^2)^(2^5)^(2^0)^(1^10)^(1^12)^(1^5)^(1^0)^(3^10)^(3^2)^(3^5)^(3^0)

        # Here each number in nums1 repeats len(nums2) number of times and each number in nums2 repeats for len(nums1) number of times

        # So if len(nums1) is even, then return XOR of all items in nums2

        # If len(nums2) is even, then return XOR of all items in nums1

        # If both are even, return 0

        # If both are odd, return XOR of all items in two arrays
        
        xor = 0

        if(len(nums2) % 2 == 0):
            xor = 0
        
        if(len(nums1) % 2 != 0):
            for i in nums2:
                xor ^= i

        if(len(nums1) % 2 == 0):
            xor = 0
        
        if(len(nums2) % 2 != 0):
            for i in nums1:
                xor ^= i
        
        return xor