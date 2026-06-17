# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        elif n == 1:
            return lists[0]
        def sort(lt,lt1):
            dummy = ListNode(0)
            dup = dummy

            while lt and lt1:
                if lt.val <= lt1.val:
                    dup.next = lt
                    lt = lt.next
                else:
                    dup.next = lt1
                    lt1 = lt1.next
                dup = dup.next
            if lt:
                dup.next = lt
            if lt1:
                dup.next = lt1
                
            return dummy.next
        lt = lists[0]
        for i in range(1,n):
            lt = sort(lt,lists[i])
           
        return lt
        