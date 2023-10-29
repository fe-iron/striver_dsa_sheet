from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or k == 0 or head.next == None:
            return head
        count = 1
        temp_head = head
        while temp_head.next != None:
            count += 1
            temp_head = temp_head.next

        temp_head.next = head
        k = k % count
        k = count - k
        while k:
            temp_head = temp_head.next
            k -= 1
        head = temp_head.next
        temp_head.next = None
        return head