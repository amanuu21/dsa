1class Solution:
2    def myAtoi(self, s: str) -> int:
3        i = 0
4        n = len(s)
5        
6        # Skip leading whitespaces
7        while i < n and s[i] == ' ':
8            i += 1
9        
10        # Check sign
11        sign = 1
12        if i < n and s[i] in ['+', '-']:
13            if s[i] == '-':
14                sign = -1
15            i += 1
16        
17        # Convert digits
18        num = 0
19        while i < n and s[i].isdigit():
20            digit = int(s[i])
21            
22            # Check overflow before adding digit
23            if num > (2**31 - 1 - digit) // 10:
24                return -2**31 if sign == -1 else 2**31 - 1
25            
26            num = num * 10 + digit
27            i += 1
28        
29        return sign * num