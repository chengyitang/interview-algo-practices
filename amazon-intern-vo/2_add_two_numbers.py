# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(0)
        cur = dummyHead
        carry = 0

        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            columnSum = x + y + carry
            carry = columnSum // 10
            digit = columnSum % 10

            cur.next = ListNode(digit)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummyHead.next
# Medium 
# Linked list, Math, Recursion
# Time: O(max(n, m))
# Space: O(max(n, m))