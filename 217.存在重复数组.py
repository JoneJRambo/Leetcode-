from typing import List

# 通过hashmap解决
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) ==0 :
            return False
        dic = {}
        for num in nums:
            if num in dic.keys():
                dic[num] += 1
            else:
                dic[num] = 1

        for value in dic.values():
            if value > 1:
                return True
        else:
            return False



solution = Solution()
nums=[2,14,18,22,22]
print(solution.containsDuplicate(nums))