class Solution:
    def trap(self, height: List[int]) -> int:
        """
        动态规划
        """
        if not height:
            return 0

        n = len(height)
        left, right = [0]*n, [0]*n
        ans = 0

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        right[n-1] = height[n-1]
        for i in range(n-2, 0, -1):
            right[i] = max(right[i+1], height[i])

        for i in range(1, n-1):
            ans += min(left[i], right[i]) - height[i]
        
        return ans
    
    def trap2(self, height: List[int]) -> int:
        """
        双指针
        """
        if not height:
            return 0
        
        left, right = 0, len(height)-1
        l_max, r_max = 0, 0
        ans = 0

        while left < right:
            if height[left] < height[right]:
                l_max = max(l_max, height[left])
                ans += l_max-height[left]
                left += 1
            else:
                r_max = max(r_max, height[right])
                ans += r_max-height[right]
                right -= 1
        
        return ans
    
    def trap3(self, height: List[int]) -> int:
        """
        栈
        """
        if not height:
            return 0

        ans, cur = 0, 0
        st = []

        while cur < len(height):
            while st and height[cur] > height[st[-1]]:
                top = st.pop()
                if not st:
                    break
                dis = cur - st[-1] - 1
                ans += dis * (min(height[cur], height[st[-1]]) - height[top])
            st.append(cur)
            cur += 1
        
        return ans