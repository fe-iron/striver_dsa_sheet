from typing import Node
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head):
        iter = head
        front = head
        # First round: make copy of each node,
        # and link them together side-by-side in a single list.
        # consider front variable equals to ahead
        while iter != None:
            front = iter.next
            new_node = Node(iter.val)
            iter.next = new_node
            new_node.next = front
            iter = front
        # Second round: assign random pointers for the copy nodes.
        iter = head
        while iter != None:
            if iter.random != None:
                iter.next.random = iter.random.next
            iter = iter.next.next
        # Third round: restore the original list, and extract the copy list.
        iter = head
        pseudo_head = Node(0)
        clone = pseudo_head
        while iter != None:
            front = iter.next.next
            # extract the copy
            clone.next = iter.next

            # restore the original list
            iter.next = front
            clone = clone.next

            iter = front
        return pseudo_head.next


