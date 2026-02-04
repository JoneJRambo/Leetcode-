class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum=0
        record={}
        record[0]=1
        res=0
        for num in nums:
            pre_sum+=num
            if pre_sum-k in record:
                res+=record[pre_sum-k]
            if pre_sum in record:
                record[pre_sum]+=1
            else:
                record[pre_sum]=1
        return res
        #前缀和+哈希表