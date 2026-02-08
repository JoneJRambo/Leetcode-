from collections import defaultdict
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        max_length = 0
        left = 0
        cnt = defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarrayLength([1,2,2,1,2,1,1,1,1],2))