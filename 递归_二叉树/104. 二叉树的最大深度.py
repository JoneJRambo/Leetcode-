# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 法一: 定义全局变量接受
        ans = 0

        def dfs(node, cnt):
            if node is None:
                return
            cnt += 1
            nonlocal ans
            ans = max(ans, cnt)
            dfs(node.left, cnt)
            dfs(node.right, cnt)

        dfs(root, 0)
        return ans

    # 法二: 递归
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        l_depth = self.maxDepth(root.left)
        r_depth = self.maxDepth(root.right)
        return max(l_depth, r_depth) + 1