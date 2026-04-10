1class Solution:
2    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
3        dummy = ListNode(0)
4        dummy.next = head
5        
6        fast = dummy
7        slow = dummy
8        
9        # Move fast pointer n+1 steps ahead
10        for _ in range(n + 1):
11            fast = fast.next
12        
13        # Move both pointers until fast reaches the end
14        while fast:
15            fast = fast.next
16            slow = slow.next
17        
18        # Remove the nth node from end
19        slow.next = slow.next.next
20        
21        return dummy.next