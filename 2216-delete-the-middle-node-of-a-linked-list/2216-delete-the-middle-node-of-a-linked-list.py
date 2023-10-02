class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(not head.next):
            return head.next


        temp = head
        l = 1         # Length

        while(temp.next != None):
            temp = temp.next
            l += 1
        
        slow = head
        fast = head

        if(l%2 == 1):
            while(fast.next.next.next):
                slow = slow.next
                fast = fast.next.next

        else:
            while(fast.next.next):
                slow = slow.next
                fast = fast.next.next
        
        if(slow and slow.next):
            slow.next = slow.next.next

        return head