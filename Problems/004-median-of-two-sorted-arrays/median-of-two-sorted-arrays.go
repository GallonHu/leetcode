package problem004

func findKth(A, B []int, k int) float64 {
	if len(A) == 0 {
		return float64(B[k])
	}
	if len(B) == 0 {
		return float64(A[k])
	}
	if k == 0 {
		if A[0] >= B[0] {
			return float64(B[0])
		} else {
			return float64(A[0])
		}
	}

	m, n := len(A), len(B)
	if A[m/2] >= B[n/2] {
		if k > m/2+n/2 {
			return findKth(A, B[n/2+1:], k-n/2-1)
		} else {
			return findKth(A[:m/2], B, k)
		}
	} else {
		return findKth(B, A, k)
	}
}

func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	m, n := len(nums1), len(nums2)

	if (m+n)&1 == 0 {
		return (findKth(nums1, nums2, (m+n)/2) + findKth(nums1, nums2, (m+n)/2-1)) / 2.0
	} else {
		return findKth(nums1, nums2, (m+n)/2)
	}
}
