1import heapq
2from typing import List, Optional
3
4# Definition for singly-linked list.
5# class ListNode:
6#     def __init__(self, val=0, next=None):
7#         self.val = val
8#         self.next = next
9
10class Solution:
11    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
12        heap = []
13
14        # Put the first node of each list into the heap
15        for i, node in enumerate(lists):
16            if node:
17                heapq.heappush(heap, (node.val, i, node))
18
19        dummy = ListNode(0)
20        current = dummy
21
22        while heap:
23            val, i, node = heapq.heappop(heap)
24
25            current.next = node
26            current = current.next
27
28            if node.next:
29                heapq.heappush(heap, (node.next.val, i, node.next))
30
31        return dummy.next