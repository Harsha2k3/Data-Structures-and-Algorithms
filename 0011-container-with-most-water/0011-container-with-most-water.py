class Solution:
    def maxArea(self, height):

        # i = 0 
        # j = len(height) - 1
        # area = -1000000

        # while i < j:
        #     area = max(area , min(height[i], height[j]) * (j - i))

        #     # Next remove the smaller one of the two lines 
        #     # from consideration
        #     if height[i] < height[j]:
        #         i += 1
            
        #     else:
        #         j -= 1
        
        # return area

        # # Why we have to remove smaller one everytime
        # # Take 1st test case
        # # height[i] = 1 and height[j] = 7
        # # Now if we remove 7 instead of 1
        # # Area for 1 and the one before 7 will be maximum of
        # # 7 x 1 = 7 unit if 1 is shorter than the one before 7
        # # or if the one before 7 is shorter than 1 then area is < 7
        # # Even if area < 7, before area i.e, 8 x 1 = 8 will be 
        # # maximum any how
        # # So remove smallest one everytime

        # # So if we remove smaller one
        # # We will get more height one for the same width
        # # i.e, 1 and 7
        # # If we remove 1 and move to 8 or if we reomve 7 and move to 3 
        # # Width between 8 and 7 = width between 1 and 3
        # # So to maximize area we can remove low height one
        # # and multiply the same width with high height one out
        # # of height[i] and height[j]


        l , r = 0 , len(height) - 1
        res = 0

        while l < r:
            area = (r - l) * min(height[r] , height[l])
            res = max(res , area)

            if height[l] < height[r]:
                l += 1
            # elif height[l] > height[r]:
            #     r -= 1
            else:
                r -= 1
        
        return res