# Definition for a binary tree node.
import time


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

if __name__ == "__main__":
    s = Solution()
    print(s.inorderTraversal(TreeNode(1, None, TreeNode(2, TreeNode(3)))))




    # 打印当前时间 以年-月-日 时分秒形式显示
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))