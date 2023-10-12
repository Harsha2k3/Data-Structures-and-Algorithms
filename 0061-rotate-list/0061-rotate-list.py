class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        temp = head
        l = 0

        while(temp):
            l += 1
            temp = temp.next

        if(k == 0 or k == l or l == 1):
            return head

        temp = head

        if(l-k-1 > 0):
            for i in range(l-k-1):
                if(temp): temp = temp.next
        else:
            if l == 0:
                t = 0
            else:
                t = (l-k-1) % l

            if(t == l-1):
                return head

            for i in range(t):
                if(temp): temp = temp.next

        if(temp):
            res = temp.next
            last = temp.next
            temp.next = None

        while(temp and last and last.next):
            last = last.next

        if(temp and last):
            last.next = head

        if(temp):
            return res