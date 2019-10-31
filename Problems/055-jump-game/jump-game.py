class Solution:
    def canJump(self, nums) -> bool:
        far = nums[0]
        for i in range(1, len(nums)-1):
            if far < i:
                break
            far = max(i + nums[i], far)

        return far >= len(nums)-1 

    def canJump2(self, nums) -> bool:
        i = len(nums) - 2
        while i >= 0:
            if nums[i] != 0:
                i -= 1
                continue

            j = i-1
            while j >= 0:
                if i-j < nums[j]:
                    i = j
                    break
                j -= 1
            
            if j == -1:
                return False
            
            i -= 1
        return True