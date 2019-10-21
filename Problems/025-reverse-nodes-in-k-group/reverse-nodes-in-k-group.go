package problem025

// ListNode definition.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	dummy := &ListNode{}
	dummy.Next = head
	pre, end := dummy, dummy

	for end.Next != nil {
		for i := 0; i < k && end != nil; i++ {
			end = end.Next
		}
		if end == nil {
			break
		}

		s, n := pre.Next, end.Next
		end.Next = nil
		pre.Next = reverse(s)
		s.Next = n
		pre, end = s, s
	}

	return dummy.Next
}

func reverse(head *ListNode) *ListNode {
	pre := &ListNode{}
	cur := head
	for cur != nil {
		next := cur.Next
		cur.Next = pre
		pre = cur
		cur = next
	}

	return pre
}
