class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        pos = []
        
        temp1 = head
        temp2 = head.next
        i = 2

        if(temp2.next):
            while(temp2.next):
                if((temp2.val > temp1.val and temp2.val > temp2.next.val) or (temp2.val < temp1.val and temp2.val < temp2.next.val)):
                    pos.append(i)

                temp1 = temp1.next
                temp2 = temp2.next
                i += 1

        if(len(pos) < 2):
            return [-1,-1]

        
        min_ = float('inf')   #  +infinity

        for i in range(1, len(pos)):
            min_ = min(min_, pos[i]-pos[i-1])

        max_ = pos[-1]-pos[0]
       
        return [min_,max_]