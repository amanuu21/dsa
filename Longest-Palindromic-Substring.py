1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if len(s) < 2:
4            return s
5        
6        start = 0
7        max_len = 1
8        
9        def expand(left: int, right: int) -> None:
10            nonlocal start, max_len
11            
12            while left >= 0 and right < len(s) and s[left] == s[right]:
13                current_len = right - left + 1
14                if current_len > max_len:
15                    start = left
16                    max_len = current_len
17                left -= 1
18                right += 1
19        
20        for i in range(len(s)):
21            # Odd length palindrome
22            expand(i, i)
23            
24            # Even length palindrome
25            expand(i, i + 1)
26        
27        return s[start:start + max_len]