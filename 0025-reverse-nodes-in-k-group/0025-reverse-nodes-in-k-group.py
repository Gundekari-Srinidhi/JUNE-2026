# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        temp = head
        i = 0 
        new_head = None
        prev_tail = None
        while i <= count - k:
            group_head = temp
            prev = None
            curr = temp
            val = k
            while curr and val != 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                i += 1
                val -= 1
            if new_head is None:
                new_head = prev
            if prev_tail:
                prev_tail.next = prev

            group_head.next = curr
            prev_tail = group_head

            temp = curr
        return new_head if new_head else head
            

