# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        
        while p.next and p.next.next:
            a, b = p.next, p.next.next
            a.next = b.next
            b.next = a
            p.next = b
            p = p.next.next

        return dummy.next