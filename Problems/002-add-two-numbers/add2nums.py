# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        res_head = ListNode(0)
        cur = res_head
        carry = 0

        while l1 or l2 or carry:
            s = carry

            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            

            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next 

        return res_head.next