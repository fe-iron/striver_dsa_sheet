# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        reverse_head = None
        next = None
        while head != None:
            next = head.next
            head.next = reverse_head
            reverse_head = head
            head = next


sol = Solution()
sol.reverseList([1,2,3,4,5])