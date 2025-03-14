class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Idea
        # Identify middle (By fast and slow pointers)
        # Reverse 2nd half
        # So, we will have seperate lists ==> 1->2 and 4->3
        # Traverse along the lists and form 1->4->2->3

        # Identifying Middle
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reversing the 2nd half

        # slow points to end of 1st half
        second = slow.next            # second half starts from second
        slow.next = None              # Seperating the 2 halves
        prev = None

        while second:
            nxt = second.next       # Saving next node
            second.next = prev
            prev = second
            second = nxt

        # Merging in required way
        first = head
        second = prev              # Now prev is at 4
        while second:
            nxt1,nxt2 = first.next,second.next  # Saving next nodes
            first.next = second
            second.next = nxt1

            first = nxt1
            second = nxt2