# 将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。
# 请你实现这个将字符串进行指定行数变换的函数：
# string convert(string s, int numRows);
# 示例 1：
# 输入：s = "PAYPALISHIRING", numRows = 3
# 输出："PAHNAPLSIIGYIR"
# 示例 2：
# 输入：s = "PAYPALISHIRING", numRows = 4
# 输出："PINALSIGYAHRPI"
# 解释：
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
# 示例 3：
# 输入：s = "A", numRows = 1
# 输出："A"
# 提示：
# 1 <= s.length <= 1000
# s 由英文字母（小写和大写）、',' 和 '.' 组成
# 1 <= numRows <= 1000
'''
垃圾版本 二维数组浪费空间
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         # 定义二维数组
#         matrix = [[''] * len(s) for _ in range(numRows)]
#         if len(s) <= numRows:
#             return s
#         # 定义写入方向
#         direction = 1  # 1向下,-1向上
#         row, col = 0, 0
#         for i in s:
#             if direction == 1:
#                 matrix[row][col] = i
#                 row += 1
#                 if row == numRows - 1:
#                     direction = -1
#                     row -= 1
#             if direction == -1:
#                 col += 1
#                 matrix[row][col] = i
#                 row -=1
#                 if row == -1:
#                     direction = 1
#                     row += 1
#         return str(matrix)
'''

# class Solution(object):
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1 or numRows >= len(s):
#             return s
#
#         # 每行用一个列表存储，只存储实际有字符的位置
#         rows = [[] for _ in range(numRows)]
#         current_row = 0
#         going_down = False
#
#         for char in s:
#             rows[current_row].append(char)
#             # 到达顶部或底部时改变方向
#             if current_row == 0 or current_row == numRows - 1:
#                 going_down = not going_down
#             # 根据方向更新行号
#             current_row += 1 if going_down else -1
#
#         # 合并所有行
#         result = []
#         for row in rows:
#             result.extend(row)
#
#         return ''.join(result)

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:  # 边界情况处理
            return s
        res = ['' for _ in range(numRows)]  # 创建结果列表
        flag, i = -1, 0  # 初始化方向和行索引
        for c in s:  # 遍历每个字符
            res[i] += c  # 将字符添加到对应行
            if i == 0 or i == numRows - 1:  # 到达边界
                flag = -flag  # 反转方向
            i += flag  # 更新行索引
        return ''.join(res)  # 连接所有行
#测试用例
solution = Solution()
s = 'ISAUGHOIUWE;PIOAOSIFDHOIHOIGHAI'
numRows = 7
print(solution.convert(s, numRows))
