package problem023

import "container/heap"

// ListNode definition.
type ListNode struct {
	Val  int
	Next *ListNode
}

type heapNode struct {
	Val int
	Idx int
}

// NodeList 堆节点
type NodeList []heapNode

func (Node NodeList) Len() int {
	return len(Node)
}

func (Node NodeList) Less(i, j int) bool {
	return Node[i].Val < Node[j].Val
}

func (Node NodeList) Swap(i, j int) {
	Node[i], Node[j] = Node[j], Node[i]
}

// Push 往 Node 中放 item
func (Node *NodeList) Push(x interface{}) {
	item := x.(heapNode)
	*Node = append(*Node, item)
}

// Pop 从 Node 中取出优先的 item
func (Node *NodeList) Pop() interface{} {
	old := *Node
	n := len(old)
	item := old[n-1]
	*Node = old[0 : n-1]
	return item
}

// 使用堆
func mergeKLists(lists []*ListNode) *ListNode {
	dummy := &ListNode{}
	pr := dummy
	n := len(lists)
	p := make(NodeList, 0, n)

	for i := 0; i < n; i++ {
		if lists[i] != nil {
			heap.Push(&p, heapNode{Val: lists[i].Val, Idx: i})
			lists[i] = lists[i].Next
		}
	}

	for len(p) != 0 {
		item := heap.Pop(&p).(heapNode)
		pr.Next = &ListNode{Val: item.Val, Next: nil}
		pr = pr.Next

		if lists[item.Idx] != nil {
			heap.Push(&p, heapNode{Val: lists[item.Idx].Val, Idx: item.Idx})
			lists[item.Idx] = lists[item.Idx].Next
		}
	}

	return dummy.Next
}

// 归并
func mergeKLists2(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}
	return merge(lists, 0, len(lists)-1)
}

func merge(lists []*ListNode, left, right int) *ListNode {
	if left == right {
		return lists[left]
	}

	mid := (left + right) / 2
	lList := merge(lists, left, mid)
	rList := merge(lists, mid+1, right)
	return mergeTwoLists(lList, rList)
}

func mergeTwoLists(l1, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}

	dummy := new(ListNode)
	head := dummy

	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			head.Next = l1
			head = head.Next
			l1 = l1.Next
		} else {
			head.Next = l2
			head = head.Next
			l2 = l2.Next
		}
	}

	if l1 != nil {
		head.Next = l1
	}
	if l2 != nil {
		head.Next = l2
	}

	return dummy.Next
}
