class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, temp):
            if not nums:
                res.append(temp)
                return
            
            for i in range(len(nums)):
                # 剪枝
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i]+nums[i+1:], temp+[nums[i]])

        res = []
        nums.sort()
        backtrack(nums, [])

        return res