# Definition for singly-linked list.
from typing import Optional
"""
        给你链表的头结点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。
        k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。
        你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
        输入：head = [1,2,3,4,5], k = 2
        输出：[2,1,4,3,5]
        输入：head = [1,2,3,4,5], k = 3
        输出：[3,2,1,4,5]
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur =  head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(0, head)
        p0 = dummy
        pre = None
        cur = p0.next
        while n>=k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        return dummy.next

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    k = 2
    res = s.reverseKGroup(head, k)
    while res:
        print(res.val)
        res = res.next
