from typing import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SolutionBetter:
    def removeNthFromEnd(self, head, n):
        if head.next == None and n == 1:
            return None
        temp_head = head
        count = 0
        while temp_head != None:
            count += 1
            temp_head = temp_head.next
        if count - n >= 0:
            n = (count - n) + 1
            count = 0
            temp_head = head
            prev_node = head
            while temp_head != None:
                count += 1
                if count == n:
                    prev_node.next = temp_head.next
                    break
                prev_node = temp_head
                temp_head = temp_head.next
        return head


class SolutionOptimal:
    def removeNthFromEnd(self, head, n):
        start = ListNode()
        start.next = head
        slow_tortoise, fast_tortoise = start
        count = 0
        while fast_tortoise != None:
            count += 1
            if count <= n:
                fast_tortoise = fast_tortoise.next
            else:
                slow_tortoise = slow_tortoise.next
                fast_tortoise = fast_tortoise.next
        slow_tortoise.next = slow_tortoise.next.next
        return start.next