class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        lenA, lenB = 0, 0
        tempA, tempB = headA, headB

        # Calculate the lengths of both linked lists
        while tempA:
            lenA += 1
            tempA = tempA.next

        while tempB:
            lenB += 1
            tempB = tempB.next

        
        tempA, tempB = headA, headB

        # Move the pointer of the longer list ahead by the absolute difference in lengths
        # By this, longer linkedlist pointer gets near head of the
        # shorter link list

        if lenA > lenB:
            for i in range(lenA - lenB):
                tempA = tempA.next
        elif lenB > lenA:
            for i in range(lenB - lenA):
                tempB = tempB.next

        # Traverse both lists together to find the intersection
        while tempA != tempB:
            tempA = tempA.next
            tempB = tempB.next

        return tempA


    #     class Solution:
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #     first_set=set()
    #     curr=headA
        
    #     while curr:
    #         first_set.add(curr)
    #         curr=curr.next
        
    #     curr = headB
    #     while curr:
    #         if curr in first_set:
    #             return curr
    #         curr=curr.next

    #     return None

    # Declare an empty set
    # set a temp pointer to head of the first linked list
    # Add all the temps to the set by traversing along the first linked list
    # Now traverse along the 2nd linked list and in every iteration check if the current pointer pointing towards the node in 2nd linked list is there in the set, of it's there return it