class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l_nums = len(nums)
        ans = nums[0]
        for i in range(1, l_nums):
            nums[i] = nums[i] + max(nums[i - 1], 0)
            ans = max(nums[i], ans)
        return ans