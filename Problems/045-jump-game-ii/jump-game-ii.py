class Solution:
    def jump(self, nums: List[int]) -> int:
        i, cnt, end = 0, 0, len(nums)-1
        nextI, maxNextI, maxI = 0, 0, 0

        while i < end:
            if i+nums[i] >= end:
                return cnt+1
            
            nextI, maxNextI = i+1, i+nums[i]
            while nextI <= maxNextI:
                if nextI+nums[nextI] > maxI:
                    maxI, i = nextI+nums[nextI], nextI
                
                nextI += 1
            
            cnt += 1
        
        return cnt


print(Solution().jump([2, 3, 1, 1, 4]))