class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        i = 0
        j = len(nums) - 1
        while i <= j:
            mid = (i + j) >> 1
            if nums[mid] == target:
                return mid
            if nums[i] == target:
                return i
            if nums[j] == target:
                return j
            if nums[i] > nums[mid]:
                if nums[j] > target > nums[mid]:
                    i = mid + 1
                else:
                    j = mid - 1
            else:
                if nums[i] < target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
        return -1