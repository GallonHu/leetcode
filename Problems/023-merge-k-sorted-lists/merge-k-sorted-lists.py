# Definition for singly-linked list.
import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        堆
        """
        dummy = ListNode(0)
        p = dummy

        pq = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(pq, (l.val, i))
                lists[i] = lists[i].next
        
        while pq:
            val, idx = heapq.heappop(pq)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(pq, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        
        return dummy.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        """
        归并
        """
        if not lists: return
        return self.merge(lists, 0, len(lists)-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) // 2
        
        llist = self.merge(lists, left, mid)
        rlist = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(llist, rlist)

    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

