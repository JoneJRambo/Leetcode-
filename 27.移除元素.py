from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        # 双指针
        l = 0
        r = len(nums) - 1
        while l < r:
            while l<r and nums[l] != val:
                l += 1
            while l <r and nums[r] == val:
                r -= 1
            nums[l], nums[r] = nums[r], nums[l]
        if nums[l] == val:
            return l
        else:
            return l+1

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         for i in nums.copy():
#             if i == val:
#                 nums.remove(i)
#         k = len(nums)
#         return k

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 快慢指针 - 最简单高效
        k = 0  # 新数组长度/慢指针
        for i in range(len(nums)):  # i是快指针
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,1,3,4,3,1]
    val =3
    result = s.removeElement(nums, val)
    print(result)
