from itertools import count
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        num_max = max(nums)
        ans, left, cnt = 0, 0, 0
        for x in nums:
            if x == num_max:
                cnt += 1
            while cnt == k:
                if nums[left] == num_max:
                    cnt -= 1
                left += 1
            ans += left
        return ans





if __name__ == '__main__':
    s = Solution()
    print(s.countSubarrays([2, 2, 2, 2, 2, 2, 2, 2], 2))

"""
示例 1：
输入：nums = [1,3,2,3,3], k = 2
输出：6
解释：包含元素 3 至少 2 次的子数组为：[1,3,2,3]、[1,3,2,3,3]、[3,2,3]、[3,2,3,3]、[2,3,3] 和 [3,3] 。

例如示例 1，当右端点移到第二个 3 时，左端点移到 2，此时 [1,3,2,3] 和 [3,2,3] 是满足要求的。
当右端点移到第三个 3 时，左端点也移到第三个 3，此时 [1,3,2,3,3],[3,2,3,3],[2,3,3],[3,3] 都是满足要求的。所以答案为 2+4=6。
"""
