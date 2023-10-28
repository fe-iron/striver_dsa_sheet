from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False
        slow_tortoise = fast_tortoise = head
        while fast_tortoise.next != None and fast_tortoise.next.next != None:
            slow_tortoise = slow_tortoise.next
            fast_tortoise = fast_tortoise.next.next
            if slow_tortoise == fast_tortoise:
                return True
        return False