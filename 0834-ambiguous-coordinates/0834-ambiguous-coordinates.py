class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:

        nums = s[1 : -1]
        
        def is_valid(num):

            if '.' in num:
                left,  right = num.split('.')
                return (left == '0' or not left.startswith('0')) and not right.endswith('0')

            return num == '0' or not num.startswith('0')
        
        def get_possible_nums(num):

            nums = []

            if is_valid(num):
                nums.append(num)

            for i in range(1 , len(num)):

                if is_valid(num[ : i] + '.' + num[i : ]):
                    nums.append(num[ : i] + '.' + num[i : ])
                    
            return nums
        
        res = []

        for i in range(1 , len(nums)):

            left = nums[ : i]
            right = nums[i : ]

            lnums = get_possible_nums(left)
            rnums = get_possible_nums(right)

            for l in lnums:
                for r in rnums:
                    res.append("(" + l + ", " + r + ")")
        
        return res