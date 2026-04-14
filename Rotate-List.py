1# Definition for singly-linked list.
2class ListNode:
3    def __init__(self, val=0, next=None):
4        self.val = val
5        self.next = next
6
7class Solution:
8    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
9        # Edge cases: empty list, single node, or no rotation needed
10        if not head or not head.next or k == 0:
11            return head
12        
13        # Step 1: Find the length of the list
14        length = 1
15        tail = head
16        while tail.next:
17            tail = tail.next
18            length += 1
19        
20        # Step 2: Optimize k (handle cases where k > length)
21        k = k % length
22        if k == 0:
23            return head
24        
25        # Step 3: Find the new head (node at position length - k)
26        # We need to find the node that will become the new tail
27        new_tail_position = length - k - 1
28        new_tail = head
29        
30        for _ in range(new_tail_position):
31            new_tail = new_tail.next
32        
33        # Step 4: Perform the rotation
34        new_head = new_tail.next
35        new_tail.next = None
36        tail.next = head
37        
38        return new_head