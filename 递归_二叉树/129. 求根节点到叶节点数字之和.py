# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_sum):
            if not node:
                return 0
            # 更新路径值
            current_sum = current_sum * 10 + node.val
            # 如果是叶子节点，返回当前路径值
            if not node.left and not node.right:
                return current_sum

            # 否则返回左右子树的和
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        return dfs(root, 0)


