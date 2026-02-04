# class Solution:
#     def myAtoi(self, s: str) -> int:
#         # 先去前导空格
#         s = s.lstrip()
#
#         if not s:
#             return 0
#
#         # 处理符号
#         sign = 1
#         if s[0] in '+-':
#             sign = -1 if s[0] == '-' else 1
#             s = s[1:]
#
#         # 读取数字
#         str1 = ''
#         for char in s:
#             if char.isdigit():
#                 str1 += char
#             else:
#                 break
#
#         if not str1:
#             return 0
#
#         # 转换为整数
#         num = sign * int(str1)
#
#         # 处理溢出
#         INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1
#         if num < INT_MIN:
#             return INT_MIN
#         if num > INT_MAX:
#             return INT_MAX
#
#         return num

import re
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        str = str.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(str)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值

if __name__ == '__main__':
    s = Solution()
    s1 = '983495__- - 94cd'
    print(s.myAtoi(s1))
