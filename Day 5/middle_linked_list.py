import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Better
class Solution:
    def middleNode(self, head):
        temp_node = head
        count = 0
        while temp_node != None:
            count += 1
            temp_node = temp_node.next
        count = (count/2)+1 if count % 2 == 0 else count / 2
        count = math.ceil(count)
        i = 0
        while head != None:
            i += 1
            if i == count:
                return head
            head = head.next


class SolutionOptimal:
    def middleNode(self, head):
        slow_tortoise = fast_tortoise = head
        while fast_tortoise.next != None and fast_tortoise != None:
            fast_tortoise.next = fast_tortoise.next.next
            slow_tortoise = slow_tortoise.next
            

sol = Solution()
sol.middleNode(head)