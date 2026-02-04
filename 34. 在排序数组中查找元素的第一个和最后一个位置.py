from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lowerbound(nums: List[int], target: int) -> int:
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        start = lowerbound(nums, target)
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        end = lowerbound(nums, target + 1)

        return [start, end - 1]

if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5, 7, 7, 8, 8, 10], 8))