class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head:              # if head == None
            return False

        slow = head
        fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
