from typing import List

from skimage.data import brain


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # if len(nums) < 4:
        #     return []
        #
        # nums.sort()
        # n = len(nums)
        # result = []
        # # 三数窗口
        # for i in range(n - 3):
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     for j in range(i + 1, n - 2):
        #         if j > i + 1 and nums[j] == nums[j - 1]:
        #             continue
        #
        #         for k in range(j + 1, n - 1):
        #             if k > j + 1 and nums[k] == nums[k - 1]:
        #                 continue
        #             three_sum = nums[i] + nums[j] + nums[k]
        #             need = target - three_sum
        #             remaining_nums = set(nums[k + 1:])
        #             if need in remaining_nums:
        #                 quad = [nums[i], nums[j], nums[k], need]
        #                 if quad not in result:
        #                     result.append(quad)
        # return result


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        # 第一个数
        for i in range(n - 3):
            x = nums[i]
            # 去重
            if i > 0 and x == nums[i - 1]:
                continue
            # 优化一 前四项加和大于target 退出循环
            if x + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            # 优化二 第一个数和后三项价格小于target 移动i
            if x + nums[-3] + nums[-2] + nums[-1] < target:
                continue
                # 第二个数
            for j in range(i + 1, n - 2):
                # 去重
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 优化三 同一
                if x + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                # 优化四 同二
                if x + nums[j] + nums[-1] + nums[-2] < target:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    if x + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    elif x + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return result

if __name__ == '__main__':
    nums = [2,2,2,2,2]
    target = 0
    solution = Solution()
    result = solution.fourSum(nums, target)
    print(result)
