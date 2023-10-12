class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if(head.val >= 5):
            new_head = ListNode(0)
            new_head.next = head
        else:
            new_head = head

        h = new_head


        while(new_head):
            new_head.val = (new_head.val * 2) % 10 + (1 if new_head.next and new_head.next.val >= 5 else 0)
            new_head = new_head.next

        return h



        # 18 % 10 ==> We will get 8
        # 14 % 10 ==> We will get 4
        # etc ...