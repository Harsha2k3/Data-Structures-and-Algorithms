class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:

        # res = []

        # for i in range(len(nums)):
            
        #     if nums[i][i] == '1':
        #         res.append('0')
        #     else:
        #         res.append('1')

        # return "".join(res)

        # # ["01" , "10"]
        # # Here nums[0][0] = 0 ==> "1"
        # #      nums[1][1] = 0 ==> "11"
        # # So, we keep checking 1st place , 2nd place so on...
        # # and we add the opposite number (we add "1" if "0" and "0" if "1")
        # # By doing so we get a new number which is not in nums


        res = ""

        def rec(l):

            nonlocal res

            if len(l) == len(nums):
                if "".join(l) not in nums and res == "":
                    res =  "".join(l)
                return

            l.append("0")
            rec(l)
            l.pop()
            l.append("1")
            rec(l)
            l.pop()
        
        rec([])

        return res