import collections

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        count = collections.defaultdict(int)
        
        start = 0
        end = 0
        max_fruit = 0
        tot = 0
        
        while(end < len(fruits)):
            if((len(count) <= 2)):
                count[fruits[end]] += 1
                tot += 1
                
                end += 1

            while(len(count) > 2):
                # Until the count is greater than 2, keep on shrinking the Sliding Window
                count[fruits[start]] -= 1
                tot -= 1

                if(count[fruits[start]] == 0):
                    count.pop(fruits[start])

                start += 1

            max_fruit = max(max_fruit,tot)
        
        return max_fruit

        # Maintain a hashmap
        # Store the number(key) and it's count(value) in it
        # Just expand the sliding window if len(hashmap) < 2
        # Just shrink the sliding window while len(hasmap) > 2
        # i.e, until the len(hashmap) > 2 ==> Shrink the window 