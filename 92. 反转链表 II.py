# Definition for singly-linked list.
from typing import Optional
"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。
请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
示例 1：
输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next= head)
        p0 = dummy

        for _ in range(left - 1):
            p0 = p0.next

        pre = None
        cur = p0.next

        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        p0.next.next = cur
        p0.next = pre
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)
    result = s.reverseBetween(node1, 2, 4)
    while result:
        print(result.val)
        result = result.next




