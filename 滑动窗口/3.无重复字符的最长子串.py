# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
#
# # 并集
# print(A | B)      # 输出: {1, 2, 3, 4, 5, 6}
# print(A.union(B)) # 同上
#
# # 交集
# print(A & B)      # 输出: {3, 4}
# print(A.intersection(B))  # 同上
#
# # 差集 (在A中但不在B中)
# print(A - B)      # 输出: {1, 2}
# print(A.difference(B))  # 同上
#
# # 对称差集 (在A或B中，但不同时在两者中)
# print(A ^ B)      # 输出: {1, 2, 5, 6}
import time


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            print(char_set)
            max_length = max(max_length, right - left + 1)

        return max_length

solution = Solution()
s1='abcabcbbpoiasghhiowaertyp;aoslfa;'
start =time.time()
length = solution.lengthOfLongestSubstring(s1)
print(length)
end = time.time()
print(end - start)