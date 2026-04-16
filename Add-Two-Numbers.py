1class Solution:
2    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
3        dummy = ListNode(0)
4        current = dummy
5        carry = 0
6        
7        while l1 or l2 or carry:
8            val1 = l1.val if l1 else 0
9            val2 = l2.val if l2 else 0
10            
11            total = val1 + val2 + carry
12            carry = total // 10
13            digit = total % 10
14            
15            current.next = ListNode(digit)
16            current = current.next
17            
18            if l1:
19                l1 = l1.next
20            if l2:
21                l2 = l2.next
22        
23        return dummy.next