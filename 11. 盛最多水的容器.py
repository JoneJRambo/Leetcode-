class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maximum = 0
        while left < right:
            if height[left] < height[right]:
                cur = (right - left) * height[left]
                left += 1
            else:
                cur = (right - left) * height[right]
                right -= 1
            if maximum < cur:
                maximum = cur
        return maximum



