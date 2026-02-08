from cmath import inf
from typing import List


# class Solution:
#     def threeSumClosest(self, nums: List[int], target: int) -> int:
#         nums.sort()
#         n = len(nums)
#         closest_sum = float('inf')
#         min_diff = float('inf')
#         for i in range(n - 2):
#             left = i + 1
#             right = n - 1
#             while left < right:
#                 current_sum = nums[i] + nums[left] + nums[right]
#                 current_diff = abs(current_sum - target)
#                 if current_diff < min_diff:
#                     min_diff = current_diff
#                     closest_sum = current_sum
#                 if current_sum < target:
#                     left += 1
#                 elif current_sum > target:
#                     right -= 1
#                 else:
#                     return 0
#
#         return closest_sum

# 极致优化版本
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        ans = inf
        for i in range(n - 2):
            x = nums[i]
            # 优化
            if i and x == nums[i - 1]:
                continue

            # 优化
            s = x + nums[i + 1] + nums[i + 2]
            if s > target:  # 后面无论怎么选，选出的三数之和不会比 s 还小
                if s - target < abs(ans - target):
                    ans = s
                break

            # 优化
            s = x + nums[-2] + nums[-1]
            if s < target:  # x 加上后面任意两个数都不超过 s，所以下面的双指针就不需要跑了
                if target - s < abs(ans - target):
                    ans = s
                continue

            # 双指针
            j, k = i + 1, n - 1
            while j < k:
                s = x + nums[j] + nums[k]
                if s == target:
                    return target
                if abs(s - target) < abs(ans - target):  # s 离 target 更近
                    ans = s
                if s > target:
                    k -= 1
                else:  # s < target
                    j += 1
        return ans

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    target = 2
    solution = Solution()
    print(solution.threeSumClosest(nums, target))




