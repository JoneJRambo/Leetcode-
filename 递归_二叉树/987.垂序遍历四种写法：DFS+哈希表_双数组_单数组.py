"""
看示例 3，我们需要知道每个节点的行号 row、列号 col 以及节点值 val。
如果知道了这些信息，那么问题相当于，给你这些三元组：
(2,−2,4),(1,−1,2),(0,0,1),(2,0,6),(2,0,5),(1,1,3),(2,2,7)
每个三元组表示 (row,col,val)，你需要把这些三元组按照 col 分组，也就是把 col 相同的
分到同一组，每组只保留 val，每组的 val 按照 row 从小到大排序，row 相同的按照 val
从小到大排序。分组后的结果就是答案 [[4],[2],[1,5,6],[3],[7]]。

为了获取每个节点的信息，我们可以用 DFS，除了参数 node 外，还需要参数 row 和 col
表示当前节点的行号和列号。每往下递归一层，就把 row 加一。如果往左儿子递归，就把
col 减一；如果往右儿子递归，就把 col 加一。

在 DFS 的同时，用一个哈希表（或者有序字典）来记录这些数据。哈希表的 key 是 col，
哈希表的 value 是一个列表，列表中保存 (row,val) 二元组。

DFS 结束后，按照 key 从小到大遍历哈希表，对于哈希表的每个 value，把 value 中的二元
组排序，最后取出 value 中的 val 加入答案。

"""
from collections import defaultdict

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 法一:
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        groups = defaultdict(list)

        def dfs(node: Optional[TreeNode], row: int, col: int):
            if node is None:
                return
            groups[col].append((row, node.val))  # col 相同的分到同一组
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        ans = []
        for _, g in sorted(groups.items()):
            g.sort()  # 按照 row 排序，row 相同按照 val 排序
            ans.append([val for _, val in g])
        return ans


# 法二:
# 也可以在 DFS 的同时记录 col 的最小值，这样无需对 key 排序，也无需使用有序字典。
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        groups = defaultdict(list)
        min_col = 0

        def dfs(node: Optional[TreeNode], row: int, col: int):
            if node is None:
                return
            nonlocal min_col
            min_col = min(min_col, col)
            groups[col].append((row, node.val))  # col 相同的分到同一组
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        ans = []
        for col in range(min_col, min_col + len(groups)):
            g = groups[col]
            g.sort()  # 按照 row 排序，row 相同按照 val 排序
            ans.append([val for _, val in g])
        return ans


# 法三:
'''
也可以用两个列表记录数据，一个列表 left 负责统计负数 col，另一个列表 right 负责统计非负数 col。
注：相当于用两个列表来模拟双端队列。
'''


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        left, right = [], []

        def dfs(node: Optional[TreeNode], row: int, col: int):
            if node is None:
                return
            if col < -len(left):
                left.append([])
            elif col == len(right):
                right.append([])
            (left[-col - 1] if col < 0 else right[col]).append((row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        ans = []
        for g in left[::-1] + right:
            g.sort()
            ans.append([val for _, val in g])
        return ans


# 法四:
# 大道至简，把所有 (col,row,val) 全部丢到同一个列表中，排序后按照 col 分组。
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        data = []

        def dfs(node: Optional[TreeNode], row: int, col: int):
            if node is None:
                return
            data.append((col, row, node.val))
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        ans = []
        last_col = float('inf')
        data.sort()
        for col, _, val in data:
            if col != last_col:
                last_col = col
                ans.append([])
            ans[-1].append(val)
        return ans
