class Solution:
    def fourSum1(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)

        i = 0
        res = []
        while i < n-3:
            j = i+1
            while j < n-2:
                k, l = j+1, n-1
                while k < l:
                    s = nums[i] + nums[j] + nums[k] + nums[l] - target
                    if s == 0:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1

                        while k < n and nums[k] == nums[k-1]:
                            k += 1
                        while k < l and nums[l] == nums[l+1]:
                            l -= 1
                    elif s > 0:
                        l -= 1
                    else:
                        k += 1
                j += 1
                while j < n-2 and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i < n-3 and nums[i] == nums[i-1]:
                i += 1
        return res

    
    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n, res, sum2index = len(nums), set(), {}

        if n < 4:
            return []
        
        nums.sort()

        for p in range(n):
            for q in range(p+1, n):
                if nums[p] + nums[q] not in sum2index:
                    sum2index[nums[p]+nums[q]] = [(p, q)]
                else:
                    sum2index[nums[p]+nums[q]].append((p, q))
        
        for i in range(n-3):
            for j in range(i+1, n-2):
                remain = target-nums[i]-nums[j]
                if remain in sum2index:
                    for p, q in sum2index[remain]:
                        if p > j:
                            res.add((nums[i], nums[j], nums[p], nums[q]))
        
        return [list(i) for i in res]