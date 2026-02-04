from typing import List

'''
双指针法
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        current_len = 1
        max_len = 1
        for i in range(1, len(nums)):
            # 跳过重复数字
            if nums[i] == nums[i - 1]:
                continue
            # 如果是连续数字
            if nums[i] == nums[i - 1] + 1:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                # 中断了，重置当前长度
                current_len = 1
        return max_len
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            # 只检查可能是序列起点的数字
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest = max(longest, current_streak)

        return longest

if __name__ == '__main__':
    s = Solution()
    nums = [100, 4, 200, 1, 3, 2]
    nums1 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] #
    print(s.longestConsecutive(nums))
    print(s.longestConsecutive(nums1))
