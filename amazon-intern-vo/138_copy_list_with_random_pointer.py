"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.old2new = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # TO-DO: check null
        if not head:
            return None

        if head in self.old2new:
            return self.old2new[head]

        node = Node(head.val, None, None) # copy a new ndoe

        self.old2new[head] = node # match new node to new old node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        
        return node

# Medium. Hashmap, DFS recursive, linked list.
# Time: O(n)
# Space: O(n)

# Follow up: O(1) space
# Traverse the original list and clone the nodes as you go and place the cloned copy next to its original node.
# Then traverse the list again and adjust the pointers for the random pointers.
# Finally, extract the cloned list from the original list.

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
        
        cur = head
        while cur:

            # clone node
            new_node = Node(cur.val, None, Nonde)

            # place the clone node next to the riginal one
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next

        cur = head
        while cur:
            if cur.random: # original node
                cur.next.random = cur.random.next
                cur = cur.next.next

        ptr_old = head
        ptr_new = head.next
        head_new = head.next
        while ptr_old:
            # split the new/old lists
            ptr_old.next = ptr_old.next.next
            ptr_new.next = (ptr_new.next.next if ptr_new.next else None)
            # update pointers
            ptr_old = ptr_old.next
            ptr_new = ptr_new.next
                
        return head_new
    
# Medium. Linked list.
# Time: O(n)
# Space: O(1)
    