1class Solution:
2    def divide(self, dividend: int, divisor: int) -> int:
3        # Edge case: division by zero (not in constraints but good practice)
4        if divisor == 0:
5            return float('inf')
6        
7        # Handle overflow edge case
8        if dividend == -2**31 and divisor == -1:
9            return 2**31 - 1
10        
11        # Determine sign
12        negative = (dividend < 0) ^ (divisor < 0)
13        
14        # Work with absolute values
15        a = abs(dividend)
16        b = abs(divisor)
17        
18        quotient = 0
19        
20        # Subtract multiples of b from a using bit shifts
21        while a >= b:
22            temp = b
23            multiple = 1
24            # Double the divisor until it's too big
25            while a >= (temp << 1):
26                temp <<= 1
27                multiple <<= 1
28            # Subtract the largest multiple found
29            a -= temp
30            quotient += multiple
31        
32        # Apply sign
33        if negative:
34            quotient = -quotient
35        
36        # 32-bit integer range check
37        if quotient > 2**31 - 1:
38            return 2**31 - 1
39        if quotient < -2**31:
40            return -2**31
41        
42        return quotient