# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        # 使用 DFS 遍历，记录 (col, row, val)
        nodes = []

        def dfs(node, col, row):
            if not node:
                return
            nodes.append((col, row, node.val))
            dfs(node.left, col - 1, row + 1)  # 向左：col-1
            dfs(node.right, col + 1, row + 1)  # 向右：col+1

        dfs(root, 0, 0)

        # 排序：先按列，再按行，再按值
        nodes.sort(key = lambda x: (x[0], x[1], x[2]))

        # 按列分组返回
        result = []
        current_col = None
        current_group = []
        for col, row, val in nodes:
            if col != current_col:
                # 新列开始，保存上一列的结果
                if current_group:
                    result.append(current_group)
                current_group = [val]
                current_col = col
            else:
                # 同一列，添加到当前组
                current_group.append(val)

        # 添加最后一列
        if current_group:
            result.append(current_group)

        return result

