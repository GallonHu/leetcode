class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        res = []
        i = 0
        while i < n-2 and nums[i] <= 0:
            j, k = i+1, n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # 去重
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif s < 0:
                    j += 1
                else:
                    k -= 1

            i += 1
            # 去重
            while i < n-2 and nums[i] == nums[i-1]:
                i += 1
        
        return res
