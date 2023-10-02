class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)  
        temp = dummy  
        
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next

            # We update list1 and list2 based on which value is
            # less among list1.val and list2.val to keep the 
            # resultant list sorted
            temp = temp.next
        
        # Attach the remaining nodes, if any, from list1 or list2
        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
        
        return dummy.next  # Return the head of the merged list