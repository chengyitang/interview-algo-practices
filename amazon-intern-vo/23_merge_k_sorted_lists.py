# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        values = []
        dummy_head = point = ListNode(0)
        for l in lists: # O(n)
            while l:
                values.append(l.val)
                l = l.next

        for value in sorted(values): # O(n log n) + O(n)
            point.next = ListNode(value)
            point = point.next

        return dummy_head.next
# Time: O(n log n)
# Space: O(n)

# Follow up: 