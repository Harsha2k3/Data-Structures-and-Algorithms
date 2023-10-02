class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = head
        fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                # If the pointers meet, there is a cycle in the linked list.
                # Reset the slow pointer to the head of the linked list, and move both pointers one step at a time
                # until they meet again. The node where they meet is the starting point of the cycle.
                while(slow != fast):
                    slow = slow.next
                    fast = fast.next
                return slow   # or return fast

        return None