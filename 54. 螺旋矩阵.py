import copy
from typing import List


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return []
#         result = []
#
#         def spiral(matrix):
#             if not matrix or not matrix[0]:
#                 return []
#             m, n = len( matrix), len(matrix[0])
#             # 正序取第一行
#             result.extend(matrix[0])
#             # 删除第一行
#             del matrix[0]
#             m -= 1
#             if m == 0:
#                 return
#
#             # 取最后一列(第二行至倒数第二行最后一个数)
#             # 目前行数有变化,原来第二行是现在的第一行
#             if m >1:
#                 for i in range(m-1):
#                     result.append(matrix[i][n-1])
#                 # 删除最后一列
#                 for i in range(m-1):
#                     del matrix[i][n-1]
#                 n -= 1
#
#             # 取最后一行
#             if m >1: # 至少有两行
#                 result.extend(matrix[m-1][::-1])
#                 del matrix[m-1]
#                 m -= 1
#
#             spiral( matrix)
#
#         mat_copy =copy.deepcopy(matrix)
#         spiral(mat_copy)
#         return result



# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix or not matrix[0]:
#             return []
#
#         result = []
#         m, n = len(matrix), len(matrix[0])
#         top, bottom, left, right = 0, m - 1, 0, n - 1
#
#         while top <= bottom and left <= right:
#             # 1. 第一行全部
#             for col in range(left, right + 1):
#                 result.append(matrix[top][col])
#
#             # 2. 中间行（第二行到倒数第二行）取最后一个数
#             # 注意：这里只取每行的最后一个数，不是整列
#             if top + 1 <= bottom - 1:  # 还有中间行
#                 for row in range(top + 1, bottom):  # top+1 到 bottom-1
#                     result.append(matrix[row][right])
#
#             # 3. 最后一行逆序（如果最后一行不是第一行）
#             if top < bottom:
#                 for col in range(right, left - 1, -1):
#                     result.append(matrix[bottom][col])
#
#             # 4. 中间行（倒数第二行到第二行）取第一个数
#             # 注意：这里只取每行的第一个数，不是整列
#             if top + 1 <= bottom - 1 and left < right:  # 有中间行且列不重复
#                 for row in range(bottom - 1, top, -1):  # bottom-1 到 top+1
#                     result.append(matrix[row][left])
#
#             # 收缩边界，进入内层
#             top += 1
#             bottom -= 1
#             left += 1
#             right -= 1
#
#         return result

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        count_s=len(matrix)+len(matrix[0])
        list1=[]
        for i in range(count_s):
            list1.append(matrix.pop(0))
            if matrix == []:
                break
            else:
                matrix=[[row[i] for row in matrix] for i in range(len(matrix[0]))][::-1]
        return list(j for i in list1 for j in i)



if __name__ == "__main__":
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.spiralOrder(matrix))