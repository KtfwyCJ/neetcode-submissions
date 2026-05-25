# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0) # 值是0的头节点
        dummy.next = head

        # 快慢指针
        slow = dummy
        fast = dummy

        # fast比slow快n+1步，当fast为none时,slow.next = slow.next.next就可以了

        for _ in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next
        
