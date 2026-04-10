1class Solution:
2    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
3        dummy = ListNode(0)
4        dummy.next = head
5        prev = dummy
6
7        while prev.next and prev.next.next:
8            first = prev.next
9            second = prev.next.next
10
11            # Swapping the nodes
12            first.next = second.next
13            second.next = first
14            prev.next = second
15
16            # Move prev two nodes ahead
17            prev = first
18
19        return dummy.next