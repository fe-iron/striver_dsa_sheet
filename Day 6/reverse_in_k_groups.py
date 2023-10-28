from typing import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode()
        dummy.next = head
        cur = nxt = prev = dummy 
        count = 0
        while cur != None:
            count += 1
            cur = cur.next

        while count >= k:
            cur = prev.next
            nxt = cur.next
            for i in range(1, k):
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = cur.next
            prev = cur
            count -= k
        return dummy.next
