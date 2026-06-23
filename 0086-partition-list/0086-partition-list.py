# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftDummy = ListNode(0)
        rightDummy = ListNode(0)

        left = leftDummy
        right = rightDummy

        temp = head

        while temp:
            if temp.val < x:
                left.next = temp
                left = left.next
                temp = temp.next
            
            elif temp.val >= x:
                right.next  = temp
                right = right.next
                temp = temp.next

        if right:
            left.next = rightDummy.next
            right.next = None

        return leftDummy.next

        
        