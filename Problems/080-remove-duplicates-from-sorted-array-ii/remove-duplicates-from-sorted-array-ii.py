class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2: return len(nums)

        idx = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[idx-1]:
                idx += 1
                nums[idx] = nums[i]
                
        return idx+1