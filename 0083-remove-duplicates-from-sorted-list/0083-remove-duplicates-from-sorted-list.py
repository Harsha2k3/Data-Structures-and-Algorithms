class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        
        temp = head

        while temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return head



        # if not head or not head.next:
        #     return head
        
        # temp = head
        
        # while temp.next:
        #     if temp.val == temp.next.val:   # current value == next node's value
        #         temp.next = temp.next.next
        #     else:
        #         temp = temp.next
        
        # return head