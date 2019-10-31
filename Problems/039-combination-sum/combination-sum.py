class Solution:
    def combinationSum(self, candidates: List[int], target: int)  -> List[List[int]]:
        def backtarck(remain, start, end):
            if remain == 0:
                res.append(temp[:])
                return
            
            for i in range(start, end):
                remain -= candidates[i]
                # 剪枝
                if remain < 0:
                    break
                temp.append(candidates[i])
                backtarck(remain, i, end)
                remain += temp.pop()
        
        res, temp = [], []
        # 排序可以保证剪枝的正确性
        candidates.sort()
        backtarck(target, 0, len(candidates))

        return res