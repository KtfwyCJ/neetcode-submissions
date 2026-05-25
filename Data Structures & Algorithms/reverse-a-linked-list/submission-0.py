# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 一个节点有两个东西：
        # 1. val  自己的值
        # 2. next 指向下一个节点
        prev = None
        curr = head

        while curr:
            next_node = curr.next

            curr.next = prev

            prev = curr
            curr = next_node
        
        return prev

        