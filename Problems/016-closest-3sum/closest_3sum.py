class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        i = 0
        m = 999999999
        res = nums[0] + nums[1] + nums[2]
        while i < n-2:
            if nums[i] > target / 3:
                break
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if abs(s-target) < m:
                    m = abs(s-target)
                    res = s

                if s == target:
                    return target
                elif s > target:
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                else:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
            i += 1
            while i < n-2 and nums[i] == nums[i-1]:
                i += 1
        return res