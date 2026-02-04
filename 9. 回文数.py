# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
#         temp = str(x)
#         num_str = ''
#         if temp[0] == -1:
#             return False
#         for i in range(len(temp) - 1, -1, -1):
#             if temp[i].isdigit():
#                 num_str += temp[i]
#         result = int(num_str)
#         if result == x:
#             return True
#         else:
#             return False

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         temp = str(x)
#         if temp[0] == -1:
#             return False
#         LEN = len(temp)
#         length = LEN // 2
#         for i in range(0, length):
#             if temp[i] != temp[LEN - 1 - i]:
#                 return False
#
#         return True


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         str_x = str(x)
#         return str_x == str_x[::-1]

# 非字符串转换方式
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x < 0 or x % 10 == 0:
            return False
        else:
            revertnum = 0
            while x > revertnum:
                revertnum = revertnum * 10 + x % 10
                x //= 10
            return (x == revertnum or x == revertnum // 10)

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(101))