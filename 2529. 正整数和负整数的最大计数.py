from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
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


        left = lowerbound(nums , 0)
        right = lowerbound(nums , 1)
        return max(left, len(nums) - right)





if __name__ == "__main__":
    s = Solution()
    print(s.maximumCount([-3, -2, -1, 0, 0, 1, 2]))