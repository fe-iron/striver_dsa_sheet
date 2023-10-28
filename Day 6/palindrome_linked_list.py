from typing import Optional, ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverse_list(head):
    pre = None
    next = None
    while head != None:
        next = head.next
        head.next = pre
        pre = head
        head = next
    return pre


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return True
        slow_tortoise = fast_tortoise = head
        # find middle of the linked list
        while fast_tortoise != None and fast_tortoise.next.next != None:
            slow_tortoise = slow_tortoise.next
            fast_tortoise = fast_tortoise.next.next
        # reversing second half of the linked list
        slow_tortoise.next = reverse_list(slow_tortoise.next)
        # move slow_toroise to right side
        slow_tortoise = slow_tortoise.next
        # comparing second half from first half
        while slow_tortoise != None:
            if slow_tortoise.val != head.val:
                return False
            slow_tortoise = slow_tortoise.next
            head = head.next
        return True

