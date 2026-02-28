from collections import defaultdict
from typing import List
"""
给你一个整数数组 nums 和一个整数 k。
返回一个 子数组 的 最小 长度，使得该子数组中出现的 不同 值之和（每个值只计算一次）至少 为 k。如果不存在这样的子数组，则返回 -1。
子数组 是数组中一个连续的 非空 元素序列。
示例 1：
输入： nums = [2,2,3,1], k = 4
输出： 2
解释：
子数组 [2, 3] 具有不同的元素 {2, 3}，它们的和为 2 + 3 = 5，这至少为 k = 4。因此，答案是 2。
示例 2：
输入： nums = [3,2,3,4], k = 5
输出： 2
解释：
子数组 [3, 2] 具有不同的元素 {3, 2}，它们的和为 3 + 2 = 5，这至少为 k = 5。因此，答案是 2。
示例 3：
输入： nums = [5,5,4], k = 5
输出： 1
解释：
子数组 [5] 具有不同的元素 {5}，它们的和为 5，这 至少 为 k = 5。因此，答案是 1。
"""

class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        min_len = float('inf')
        left = cur_sum = 0
        # 用集合记录当前窗口内的元素，快速判重
        window_elements = defaultdict(int)

        for right in range(len(nums)):
            window_elements[nums[right]] += 1
            if window_elements[nums[right]] == 1:
                cur_sum += nums[right]

            while cur_sum >= k:
                min_len = min(min_len, right - left + 1)

                window_elements[nums[left]] -= 1
                if window_elements[nums[left]] == 0:
                    cur_sum -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else -1



if __name__ == '__main__':
    s = Solution()
    # print(s.minLength([5,5,4],5))
    # print(s.minLength([3,2,3,4],5))
    nums = [154,163,156,47,151,151,22,203,149,130,115,71,3,14,30,132,208,100,125,160,36,103,125,51,187,137,157,217,53,4,146,14,20,59,224,129,161,29]
    print(s.minLength(nums, 1247))