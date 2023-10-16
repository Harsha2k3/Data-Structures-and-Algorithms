class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Maintain a list(q here)
        # Just traverse along the string and just append the
        # current character to the list if it is not in the list 
        # If char is already present in the list, just 
        # remove it from the list
        # If we have done till this, it will handle 
        # only situations where a char is repeated 
        # 2 times
        # But if it is repeated more than 2 times it'll not work
        # So, just when ever the char appears for the 2nd
        # time, just append it to a seperate list
        # So, append the char to list when it's not there in the new list too.



        l = [i for i in s]
        q = []              
        l_ = []

        for i in l:
            if(i not in q and i not in l_):
                q.append(i)
            elif(i in l_):
                continue
            else:
                l_.append(i)
                q.remove(i)

        if(q == []):
            return -1
        return l.index(q[0])