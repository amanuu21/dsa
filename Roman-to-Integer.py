1class Solution:
2    def romanToInt(self, s: str) -> int:
3        # Map Roman symbols to their values
4        roman_map = {
5            'I': 1,
6            'V': 5,
7            'X': 10,
8            'L': 50,
9            'C': 100,
10            'D': 500,
11            'M': 1000
12        }
13        
14        total = 0
15        prev_value = 0
16        
17        # Traverse from right to left
18        for char in reversed(s):
19            curr_value = roman_map[char]
20            
21            # If current value is less than previous, subtract it
22            if curr_value < prev_value:
23                total -= curr_value
24            else:
25                total += curr_value
26            
27            prev_value = curr_value
28        
29        return total