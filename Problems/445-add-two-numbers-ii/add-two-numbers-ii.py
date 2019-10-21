# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0 or l2.val == 0:
            if l1.val:
                return l1
            return l2
        
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        s = 0
        head = ListNode(0)
        while stack1 or stack2:
            if stack1:
                s += stack1.pop()
            if stack2:
                s += stack2.pop()

            head.val = s % 10
            pre = ListNode(s // 10)
            pre.next = head
            head = pre

            s //= 10
        
        if head.val == 0:
            return head.next
        return head

