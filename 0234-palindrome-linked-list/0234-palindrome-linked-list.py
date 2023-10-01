class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Here everytime head of the linked list is given 
        # as a parameter and we can create a new linked list
        # by ll = ListNode() and we can use it

        # Identifying end of 1st half

        if(not head or not head.next):
            return head

        slow = head
        fast = head.next

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the 2nd half

        # slow points to end of 1st half
        second = slow.next            # second half starts from second
        slow.next = None              # Seperating the 2 halves
        prev = None

        while(second):
            nxt = second.next       # Saving next node
            second.next = prev
            prev = second
            second = nxt

            # Now prev is at 1 and second points at None
        
        # Comparing
        first,second = head,prev 
        res = False

        while(first and second):
            if(first.val == second.val):
                res = True
            else:
                res = False
                break
            first = first.next
            second = second.next
        return res