class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, temp):
            if not nums:
                res.append(temp)
                return
            
            for i in range(len(nums)):
                backtrack(nums[:i]+nums[i+1:], temp+[nums[i]])

        res = []
        backtrack(nums, [])

        return res