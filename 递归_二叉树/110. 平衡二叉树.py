# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_depth(node):
            if not node:
                return 0
            left_depth = get_depth(node.left)
            if left_depth == -1:
                return -1
            right_depth = get_depth(node.right)
            # 判断当前节点的左右子树深度差是否大于1
            if right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1
            # 返回当前节点的深度
            return max(left_depth, right_depth) + 1
        return get_depth(root) != -1

if __name__ == '__main__':
    s = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(s.isBalanced(root))