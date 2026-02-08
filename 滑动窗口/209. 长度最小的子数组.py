from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right, ans = 0, 0, 0
        min_len = float('inf')
        while right < len(nums):
            ans += nums[right]
            while ans >= target:
                min_len = min(min_len, right - left + 1)
                ans -= nums[left]
                left += 1
            right += 1

        return min_len if min_len <= len(nums) else 0


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
