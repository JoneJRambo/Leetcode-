from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index =0
        for num in nums:
            if num!=0:
                nums[index]=num
                index+=1
        for i in range(index,len(nums)):
            nums[i]=0

if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,0,8,0,6,7,8,9.5,0,87,6,6,698,0,0,9,8,0,87,7,9,0,]
    solution.moveZeroes(nums)
    print(nums)

