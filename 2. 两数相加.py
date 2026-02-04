# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头节点，简化边界条件处理
        dummy = ListNode(0)
        # 当前节点指针，用于构建结果链表
        cur = dummy
        # 进位值，初始为0
        carry = 0

        # 循环条件：只要l1、l2还有节点，或者有进位需要处理
        while l1 or l2 or carry:
            # 获取l1当前节点的值，如果l1已为空则取0
            x = l1.val if l1 else 0
            # 获取l2当前节点的值，如果l2已为空则取0
            y = l2.val if l2 else 0

            # 计算当前位的总和：两个数字 + 进位
            total = x + y + carry
            # 计算新的进位：总和除以10的商
            carry = total // 10
            # 创建新节点，存储当前位的值：总和除以10的余数
            cur.next = ListNode(total % 10)

            # 移动当前节点指针
            cur = cur.next
            # 如果l1还有节点，移动到下一个
            if l1: l1 = l1.next
            # 如果l2还有节点，移动到下一个
            if l2: l2 = l2.next

        # 返回虚拟头节点的下一个节点（真正的结果链表头）
        return dummy.next

# 辅助函数：将列表转换为链表
def create_linked_list(nums):
    if not nums:
        return None
    head = ListNode(nums[0])
    cur = head
    for num in nums[1:]:
        cur.next = ListNode(num)
        cur = cur.next
    return head

# 辅助函数：打印链表
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == '__main__':
    s = Solution()
    l1_list = [9,9,9,9,9,9,9]
    l2_list = [9,9,9,9]
    l1 = create_linked_list(l1_list)
    l2 = create_linked_list(l2_list)
    print_linked_list(s.addTwoNumbers(l1, l2))