class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # # 2 ptr's

        # people.sort()

        # l = 0
        # r = len(people) - 1

        # # cr ==> Count right
        # count , cr = 0 , 0 

        # while l <= r:
        #     if l == r:
        #         count += 1
        #         break

        #         # Break it here
        #         # or else it enters infinite loop
        #         # Because, as while condition is l <= r
        #         # Now, l == r and also the pointers are 
        #         # not shifted any ways
        #         # So pointers stays there
            
        #     elif people[l] + people[r] > limit:
        #         r -= 1
        #         cr += 1
                
        #     else:
        #         count += 1
        #         l += 1
        #         r -= 1

        # return count + cr


        people.sort()

        l , r = 0 , len(people) - 1
        boats = 0

        while l <= r:
            remain = limit - people[r]
            r -= 1
            boats += 1

            if people[l] <= remain and l <= r:
                l += 1

        return boats