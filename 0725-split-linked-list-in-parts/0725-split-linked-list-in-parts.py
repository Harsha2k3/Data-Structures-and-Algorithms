import math

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        le = 0   # Length

        temp = head

        while(temp):
            le += 1
            temp = temp.next

        res = [None] * k

        temp = head

        i = 0

        if(k > le):

            while(temp):
                res[i] = ListNode(temp.val)
                temp = temp.next
                i += 1

        else:

            rem = le % k

            for i in range(k):
                a = temp
                for j in range(1 , math.floor(le / k) + (1 if rem > 0 else 0)):
                    if temp : temp = temp.next
                
                if temp : b = temp.next
                if temp : temp.next = None

                res[i] = a

                if rem > 0:
                    rem -= 1

                temp = b


        return res