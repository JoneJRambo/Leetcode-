from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right, ans_count = 0, 0, 0
        ans = 1
        while right < len(nums):
            ans *= nums[right]
            while left <= right and ans >= k:
                ans //= nums[left]
                left += 1
            ans_count += right - left + 1
            right += 1
        return ans_count



if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10,5,2,6],100))