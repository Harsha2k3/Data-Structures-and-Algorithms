class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(not head):
            return head

        odd = head
        even = head.next
        even_head = even

        while(even and even.next):
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head  # Connect the end of the odd list to the start of the even list

        return head

        # First we have seperated odd and even indicied nodes and then connected