class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next = head
        temp = dummy

        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        
        return dummy.next







        # dummy = ListNode(0)
        # dummy.next = head
        # temp = dummy

        # while(temp and temp.next):
        #     if(temp.next.val == val):
        #         temp.next = temp.next.next
        #     else:
        #         temp = temp.next

        # return dummy.next

        
        # # We can even use a single pointer
        # # Initially, temp is pointed to dummy node that is attached to head
        # # Until temp and temp.next are not None
        # # In every iteration check, temps next's nodes value is val
        # # If condition is True, just do temp.next = temp.next.next
        # # If condition is False, just do temp = temp.next

        # #                (or)

        # # Alternative method,

        # # Idea ==> Maintain 2 pointers
        # # Create a dummy head and give head address to it
        # # First ptr ==> Points to dummy head
        # # Second pointer ==> Points to real head
        # # Move them 1 step forward in each iteration
        # # When 2nd pointer pointed node has value equal to val
        # # Use both the pointers and remove the node pointed by
        # # 2nd pointer

        
        # # dummy_head = ListNode(0)
        # # dummy_head.next = head
        
        # # temp1 =  dummy_head
        # # temp2 = head
        
        # # while temp2:
        # #     if(temp2.val == val):
        # #         temp1.next = temp2.next
        # #     else:
        # #         temp1 = temp1.next
        # #     temp2 = temp2.next
        
        # # return dummy_head.next 
        # # Return the updated linked list starting from the next node of the dummy_head

        dummy = ListNode(0,head)
        temp = dummy

        def rec():

            nonlocal dummy,temp

            if(not temp.next):
                return dummy.next

            else:
                
                if(temp.next.val == val):
                    temp.next = temp.next.next

                else:
                    temp = temp.next

                return rec()

        return rec()