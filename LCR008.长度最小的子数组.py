# 给定一个含有n个正整数的数组和一个正整数target 找出该数组中满足其总和大于等于target的长度最小的
# 子数组[numsl, numsl + 1, ..., numsr - 1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回0 。
# 示例1：
# 输入：target = 7, nums = [2, 3, 1, 2, 4, 3]
# 输出：2
# 解释：子数组[4, 3]
# 是该条件下的长度最小的子数组。
# 示例2：
# 输入：target = 4, nums = [1, 4, 4]
# 输出：1
# 示例3：
# 输入：target = 11, nums = [1, 1, 1, 1, 1, 1, 1, 1]
# 输出：0
#from scripts.VersionStamp.bulkstamp import numStamped

# j和i一起从0开始跑,j先跑,找到大于则i+1,小于则j+1
# 复杂度维O(n)
class Solution(object):
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        ans = n + 1
        start, end = 0, 0
        total = 0
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1

        return 0 if ans == n + 1 else ans

sol = Solution()
#测试
target = 64
nums = [2, 3, 1, 2, 4, 3,32,4,2,4,5,7,12,46,4,2,3,14,2,43,12,5]
print(sol.minSubArrayLen(target, nums))