# Definition for singly-linked list.
from typing import Optional


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




