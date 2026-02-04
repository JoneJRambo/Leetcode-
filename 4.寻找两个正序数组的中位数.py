class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        length=len(nums1)
        if length % 2 == 0:
            return (nums1[int(length/2) -1] + nums1[int(length/2)])/2
        else:
            return nums1[int(length//2)]

solution = Solution()
nums1 = [1, 2]
nums2 = [3, 4]
print(solution.findMedianSortedArrays(nums1, nums2))
