package problem086

// ListNode definition.
type ListNode struct {
	Val  int
	Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	low := &ListNode{}
	high := &ListNode{}
	lowHead, highHead := low, high

	for head != nil {
		if head.Val < x {
			low.Next = head
			low = low.Next
		} else {
			high.Next = head
			high = high.Next
		}
		head = head.Next
	}

	high.Next = nil
	low.Next = highHead.Next

	return lowHead.Next
}
