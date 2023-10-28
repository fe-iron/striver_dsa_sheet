# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if head == None or head.next == None:
            return None
        slow_tortoise = fast_tortoise = head
        while fast_tortoise.next != None and fast_tortoise.next.next != None:
            fast_tortoise = fast_tortoise.next.next
            slow_tortoise = slow_tortoise.next
            if slow_tortoise == fast_tortoise:
                temp_head = head
                while temp_head != slow_tortoise:
                    temp_head = temp_head.next
                    slow_tortoise = slow_tortoise.next
                return temp_head
        return None


        