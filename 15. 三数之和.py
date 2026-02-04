from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 先排序，方便去重和使用双指针
        n = len(nums)
        ans = []

        for i in range(n - 2):  # 遍历每个元素作为第一个固定值
            if i > 0 and nums[i] == nums[i - 1]:  # 跳过重复的固定值，避免重复解
                continue

            target = -nums[i]  # 需要找两个数的和等于-target
            l, r = i + 1, n - 1  # 双指针从固定值后开始

            while l < r:  # 双指针相遇时结束
                current_sum = nums[l] + nums[r]

                if current_sum == target:  # 找到有效三元组
                    ans.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:  # 跳过左侧重复值
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:  # 跳过右侧重复值
                        r -= 1

                    l += 1  # 移动指针继续寻找
                    r -= 1

                elif current_sum < target:  # 和太小，移动左指针增大和
                    l += 1
                else:  # 和太大，移动右指针减小和
                    r -= 1

        return ans  # 返回所有不重复的三元组


if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    nums2 = [-100,-70,-60,110,120,130,160]
    print(s.threeSum(nums))
    print(s.threeSum(nums2))