# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = head  # 需要一个单独的遍历指针

        while cur:
            nxt = cur.next
            cur.next = dummy.next
            dummy.next = cur
            cur = nxt  # 关键：要移动到下一个节点

        return dummy.next
