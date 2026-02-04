# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution:
#     def goodNodes(self, root: Optional[TreeNode]) -> int:
#         # 通过栈实现,设置节点栈和最大值栈
#         stack, max_stack = [root], [root.val]
#         count = 0
#         while stack:
#             node = stack.pop()
#             max_val = max_stack.pop()
#             if node.val >= max_val:
#                 count += 1
#             if node.left:
#                 stack.append(node.left)
#                 max_stack.append(max(max_val, node.left.val))
#             if node.right:
#                 stack.append(node.right)
#                 max_stack.append(max(max_val, node.right.val))
#
#         return count

class Solution:
    def goodNodes(self,root: Optional[TreeNode], max_val=float('-inf')):
        if not root:
            return 0
        left = self.goodNodes(root.left, max(max_val, root.val))
        right = self.goodNodes(root.right, max(max_val, root.val))
        return (root.val >= max_val) + left + right
        # 如果当前节点是好节点,返回left + right + 1,否则返回left + right

