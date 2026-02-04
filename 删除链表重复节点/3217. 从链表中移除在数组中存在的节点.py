# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        set0 = set(nums)
        while cur.next:
            if cur.next.val in set0:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy.next