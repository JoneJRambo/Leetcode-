"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表
中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos
是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None
    """
    假设链表头到环入口的距离为 a，环入口到相遇点的距离为 b，相遇点到环入口的距离为 c。
    环的长度为 b + c。
    当快慢指针相遇时：慢指针走了 a + b
    快指针走了 a + b + n(b + c)（n 为快指针在环内转的圈数）
    由于快指针速度是慢指针的两倍：
    2(a + b) = a + b + n(b + c)
    => a + b = n(b + c)
    => a = n(b + c) - b
    => a = (n-1)(b + c) + c   
    这个公式意味着：从链表头到环入口的距离 a，等于从相遇点走 c 步，然后再加 n-1 圈环的长度。 
    所以，将一个指针放回链表头，另一个留在相遇点，两者每次各走一步，它们将在环入口相遇。
    """

if __name__ == '__main__':
    s = Solution()
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    print(s.detectCycle(head).val)