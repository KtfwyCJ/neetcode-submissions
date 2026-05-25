# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy node
        # tail: 当前链表最后一个节点，比如火车最后一个车厢是哪个，才能接着续
        # dummy: 假的头节点，链表第一个节点特别难处理

        dummy = ListNode() # 创建头节点
        tail = dummy #创建tail

        while list1 and list2: # 因为是排好序的，所以直接while就行
            if list1.val < list2.val: # tail赋值
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next #尾结点赋值

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next # 返回dummy.next是因为dummy是假的：dummy -> 1 -> 2 -> 3
            