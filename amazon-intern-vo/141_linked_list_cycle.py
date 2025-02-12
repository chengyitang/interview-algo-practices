# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = fast = head
        
        while fast and fast.next:
            # update before checking since both start from head
            slow = slow.next
            fast = fast.next.next
            # if they meet, there is a cycle
            if slow == fast:
                return True
        return False
    
# Easy.
# Two pointers. (Fast and slow pointers)
# Time: O(n)
# Space: O(1)
# Follow up: 
# How to find the entrance of the cycle? (Leetcode 142)
# 1. Use a set to store the nodes
# 2. Use two pointers to find the entrance
# 3. The distance from the head to the entrance is the same as the distance from the meeting point to the entrance

