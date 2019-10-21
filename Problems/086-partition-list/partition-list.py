# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        low, high = ListNode(0), ListNode(0)
        lowHead, highHead = low, high

        while head:
            if head.val < x:
                low.next = head
                low = low.next
            else:
                high.next = head 
                high = high.next
            head = head.next
        
        high.next = None
        low.next = highHead.next
        
        return lowHead.next