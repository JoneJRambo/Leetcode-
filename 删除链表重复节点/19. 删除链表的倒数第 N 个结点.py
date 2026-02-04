# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         length = 0
#         cur = head
#         while cur:
#             length += 1
#             cur = cur.next
#
#         nth_node = length - n
#         if nth_node == 0:
#             return head.next
#
#         cur = head
#         for i in range(nth_node - 1):
#             cur = cur.next
#         cur.next = cur.next.next
#         return head

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 双指针法 
        dummy = ListNode(next = head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next









if __name__ == '__main__':
    s = Solution()
