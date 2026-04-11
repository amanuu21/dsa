1class Solution:
2    def reverse(self, x: int) -> int:
3        INT_MAX = 2**31 - 1
4        INT_MIN = -2**31
5        
6        sign = -1 if x < 0 else 1
7        x = abs(x)
8        
9        rev = 0
10        
11        while x != 0:
12            digit = x % 10
13            x //= 10
14            
15            # Check overflow before multiplying
16            if rev > (INT_MAX - digit) // 10:
17                return 0
18            
19            rev = rev * 10 + digit
20        
21        return sign * rev