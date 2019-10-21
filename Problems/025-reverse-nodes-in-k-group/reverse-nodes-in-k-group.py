# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre, end = dummy, dummy
        
        while end.next:
            for i in range(k):
                if end:
                    end = end.next
            if not end:
                break
            
            start = pre.next
            next = end.next
            end.next = None
            pre.next = self.reverse(start)
            start.next = next
            pre = start

            end = pre

        return dummy.next
    
    def reverse(self, head: ListNode) -> ListNode:
        pre = ListNode(0)
        cur = head

        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre