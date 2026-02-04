from pickletools import read_unicodestringnl
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        nums.sort()
        n = len(nums)
        result = 0

        for i in range(n - 2):
            a = nums[i]
            if a == 0:
                continue

            # 优化：如果最小的两条边之和大于最大边
            if a + nums[i + 1] > nums[-1]:
                # 那么对于这个 a，所有的 b, c 组合都满足条件
                # 从剩下的 n-i-1 个数中选 2 个：C(n-i-1, 2)
                result += (n - i - 1) * (n - i - 2) // 2
                continue  # 继续下一个 a

            for j in range(i + 1, n - 1):
                b = nums[j]

                # 双指针找满足条件的最大 k
                left, right = j + 1, n - 1
                k = j  # 初始化为 j，表示没有找到

                while left <= right:
                    mid = (left + right) // 2
                    if a + b > nums[mid]:
                        k = mid  # 当前 mid 满足条件
                        left = mid + 1  # 尝试找更大的
                    else:
                        right = mid - 1

                # 统计三角形个数：从 j+1 到 k 的所有边都满足条件
                if k > j:
                    result += (k - j)

        return result
