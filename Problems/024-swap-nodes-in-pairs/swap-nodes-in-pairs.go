package problem024

// ListNode definition.
type ListNode struct {
	Val  int
	Next *ListNode
}

func swapPairs(head *ListNode) *ListNode {
	dummy := &ListNode{}
	dummy.Next = head
	p := dummy

	for p.Next != nil && p.Next.Next != nil {
		a, b := p.Next, p.Next.Next
		a.Next = b.Next
		p.Next = b
		b.Next = a
		p = p.Next.Next
	}

	return dummy.Next
}
