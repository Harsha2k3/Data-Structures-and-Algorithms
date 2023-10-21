class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        xor_of_all_nums = nums[0]

        for i in range(1,len(nums)):
            xor_of_all_nums ^= nums[i]
            
        # Now we will get 5^7
        # We have to extract 5 and 7 from it
        # So, we will now take position any bit that is set in the result of 5^7(i.e,2) and store it in i(say)
        # We will traverse across the array and find which bit has ith bit set
        # If ith bit is set, we will store all of them in an array
        # If ith bit is not set, we will store all of them in another array
        # Now, we perform XOR on both to get the desired numbers (Refer above photo)


        # We will store 1st set bit in xor_of_all_numbers
        # To do that, traverse along the number by performing right shifts top grab numbers
        i = 0
        while(xor_of_all_nums):
            if(xor_of_all_nums & 1):
                break
            xor_of_all_nums = xor_of_all_nums >> 1
            i += 1

        # Now, traverse along the array and check if ith bit is set

        mask = 1 << i
        l1 = []
        l2 = []

        for i in range(len(nums)):
            if(nums[i] & mask == mask):
                l1.append(nums[i])
            else:
                l2.append(nums[i])
            
        xor1 = l1[0]
        for i in range(1,len(l1)):
            xor1 ^= l1[i]
            
        xor2= l2[0]
        for i in range(1,len(l2)):
            xor2 ^= l2[i]
            
        return [xor1,xor2]