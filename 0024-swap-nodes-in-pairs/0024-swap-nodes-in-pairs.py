class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(not head or not head.next):
            return head

        slow = head
        fast = head.next

        res = head.next

        while(fast):
            if(fast.next == None):
                nxt = None
            else:
                nxt = fast.next.next

            s_nxt = fast.next

            if(fast.next != None and fast.next.next == None):
                slow.next = s_nxt
            else:
                slow.next = nxt
            fast.next = slow
                
            slow = s_nxt 
            fast = nxt

        return res