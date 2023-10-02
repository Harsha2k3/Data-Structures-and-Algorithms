class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # End of 1st half

        slow = head
        fast = head.next

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        # Reversing the 2nd half

        second = slow.next
        slow.next = None
        prev = None

        while(second):
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt        

        # Adding corresponding elements in both linked lists

        first,second = head,prev
        max_ = float('-inf')

        while(first and second):
            max_ = max(max_,(first.val+second.val))

            first = first.next
            second = second.next
        
        return max_