class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        temp = head
        count = 0

        connected = False  

        while temp:
            if temp.val in nums:
                if connected == False:
                    connected = True
                    count += 1
            else:
                connected = False

            temp = temp.next

        return count