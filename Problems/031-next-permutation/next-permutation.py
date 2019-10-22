class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def search(l, target):
            r = len(nums) - 1
            l -= 1
            while l+1 < r:
                mid = (l+r) // 2
                if target < nums[mid]:
                    r = mid
                else:
                    l = mid            
            return r
        
        def reverse(start):
            l, r = start, len(nums)-1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        left = len(nums) - 2
        while left >= 0 and nums[left] >= nums[left+1]:
            left -= 1
        
        reverse(left+1)
        
        if left == -1:
            return
        
        right = search(left+1, nums[left])
        nums[left], nums[right] = nums[right], nums[left]