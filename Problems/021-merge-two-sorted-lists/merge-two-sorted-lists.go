package problem021

// ListNode definition.
type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	head := dummy

	for l1 != nil && l2 != nil {
		if l1.Val <= l2.Val {
			dummy.Next = l1
			dummy = dummy.Next
			l1 = l1.Next
		} else {
			dummy.Next = l2
			dummy = dummy.Next
			l2 = l2.Next
		}
	}

	if l1 != nil {
		dummy.Next = l1
	}
	if l2 != nil {
		dummy.Next = l2
	}

	return head.Next
}
