from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right, num in enumerate(nums):
            k -= 1 - num
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1
        # left, max_len = 0, 0
        # for right, num in enumerate(nums):
        #     if num == 0:
        #         k -= 1
        #     while k < 0:
        #         if nums[left] == 0:
        #             k += 1
        #         left += 1
        #     max_len = max(max_len, right - left + 1)
        #
        # return max_len





if __name__ == '__main__':
    s = Solution()
    print(s.longestOnes([1,1,0,0,1,1,1,0,1,1,0],2))
    print(s.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1],3))
    print(s.longestOnes([0,0,0,1],4))
