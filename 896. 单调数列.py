class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if nums[0] < nums[-1]:
            return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1))
        return all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))