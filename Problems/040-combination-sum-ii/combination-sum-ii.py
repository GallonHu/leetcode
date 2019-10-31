class Solution:
    def combinationSum2(self, candidates, target: int):
        def backtrack(remain, start, end):
            if remain == 0:
                if temp:
                    res.append(temp + [])
                return
            
            for i in range(start, end):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                remain -= candidates[i]
                if remain < 0:
                    break
                temp.append(candidates[i])
                backtrack(remain, i+1, end)
                remain += temp.pop()
        
        res, temp = [], []
        candidates.sort()
        backtrack(target, 0, len(candidates))
        
        return res

print(Solution().combinationSum2([10,1,2,7,6,1,5], 8))