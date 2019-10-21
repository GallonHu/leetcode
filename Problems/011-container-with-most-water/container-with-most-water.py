class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        area = 0

        while i < j:
            temp = min(height[i], height[j]) * (j-i)
            if temp > area:
                area = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return area
            