# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # # 定义节点接受head
        # dummy = ListNode(0)
        # dummy.next = head
        # prev = dummy
        # while head is not None:
        #     if head.val == val:
        #         prev.next = head.next
        #         head = head.next
        #     else:
        #         prev = head
        #         head = head.next
        # return dummy.next


        dummy = ListNode(0,  head)
        cur = dummy
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next