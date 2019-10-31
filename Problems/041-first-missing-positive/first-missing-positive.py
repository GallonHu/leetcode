class Solution:
    def firstMissingPositive(self, nums) -> int:
        # 整理 nums ，让 nums[k] == k+1，只要 k+1 存在于 nums 中
        # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i]
        # 这样直接交换会出错，还没有找到原因
        for i in range(len(nums)):
            k = nums[i] - 1
            while 0 <= k < len(nums) and k + 1 != nums[k]:
                nums[i], nums[k] = nums[k], nums[i]
                k = nums[i] - 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1