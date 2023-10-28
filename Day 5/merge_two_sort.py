# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 == None:
                return list2
        if list2 == None:
            return list1
        if list1.val > list2.val:
             list2, list1 = list1, list2
        result = list1
        while list1 != None and list2 != None:
            temp = None
            while list1 != None and list1.val <= list2.val:
                 temp = list1
                 list1 = list1.next
            temp.next = list2
            list1, list2 = list2, list1
        return result

