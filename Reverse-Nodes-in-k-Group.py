1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6
7class Solution:
8    def reverseKGroup(self, head, k):
9        # Helper: check if there are at least k nodes left
10        def getKth(curr, k):
11            while curr and k > 0:
12                curr = curr.next
13                k -= 1
14            return curr
15
16        dummy = ListNode(0)
17        dummy.next = head
18        groupPrev = dummy
19
20        while True:
21            kth = getKth(groupPrev, k)
22            if not kth:
23                break
24
25            groupNext = kth.next
26
27            # Reverse group
28            prev = groupNext
29            curr = groupPrev.next
30
31            while curr != groupNext:
32                temp = curr.next
33                curr.next = prev
34                prev = curr
35                curr = temp
36
37            temp = groupPrev.next
38            groupPrev.next = kth
39            groupPrev = temp
40
41        return dummy.next