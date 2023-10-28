"""
    We'll use recursion and merge sort to solve this question
    merge sort to merge two adjacent bottom nodes and recursion to solve each node list recursively
"""
class Node:
    def __init__(self, val=0, next=None, child=None):
        self.data = val
        self.next = next
        self.child = child


# Don't change the code above.

def merge_list(a: Node, b:Node) -> Node:
    temp = Node()
    res = temp
    while a != None and b != None:
        if a.data < b.data:
            temp.child = a
            a = a.child
            temp = temp.child
        else:
            temp.child = b
            b = b.child
            temp = temp.child
    if a != None:
        temp.child = a
    else:
        temp.child = b
    return res.child

def recursive_flatter(head):
    if head.next == None or head == None:
        return head
    head.next = recursive_flatter(head.next)
    head = merge_list(head, head.next)
    return head


def flattenLinkedList(head: Node) -> Node:
    # Write your code here
    temp_head = recursive_flatter(head)
    return temp_head
