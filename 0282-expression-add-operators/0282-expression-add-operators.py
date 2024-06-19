class Solution:
    def addOperators(self, s: str, target: int) -> List[str]:

        # need to traverse through s
        # backtrack each case of  start index and then +,*,-
        # need empty array ofcourse
        # need curidx = i
        # need the str path to append to the arr if my --> cur_num == target
        # need the prevNum access for multiplication
        # 1 2 3 4 5 --> 1 + 2 + 3 + 4 * 5
        #               ^ ^ ^ ^ ^ ^ ^ == 10 but we wanna do 4*5 so ---
        # just do 1 + 2 + 3 + 4 + (- 4) + (4 * 5)
        # return ans
        
        res = []

        def rec(i, path, resSoFar, prevNum):
            if i == len(s):
                if resSoFar == target:
                    res.append(path)
                return
            
            for j in range(i, len(s)):
                # starting with zero?
                if j > i and s[i] == '0':
                    break
                currNum = int(s[i:j+1])

                # if cur index is 0 then simple add that number
                if i == 0:
                    rec(j + 1, path + str(currNum), resSoFar + currNum, currNum)
                else:
                    rec(j + 1, path + "+" + str(currNum), resSoFar + currNum, currNum)
                    rec(j + 1, path + "-" + str(currNum), resSoFar - currNum, -currNum)
                    rec(j + 1, path + "*" + str(currNum), resSoFar - prevNum + (prevNum * currNum), prevNum * currNum)
                    # Watch from 4:25 to 7:00 https://www.youtube.com/watch?v=WcgjFrZceU8

        rec(0, "", 0, 0)
        
        return res