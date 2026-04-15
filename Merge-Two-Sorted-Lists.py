1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
9        dummy = ListNode()
10        current = dummy
11
12        while list1 and list2:
13            if list1.val < list2.val:
14                current.next = list1
15                list1 = list1.next
16            else:
17                current.next = list2
18                list2 = list2.next
19
20            current = current.next
21
22        if list1:
23            current.next = list1
24        else:
25            current.next = list2
26
27        return dummy.next