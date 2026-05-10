1class Solution:
2    def isNumber(self, s: str) -> bool:
3        # Flags to track key parts of the number
4        seen_digit = False
5        seen_dot = False
6        seen_e = False
7        
8        # Remove leading/trailing spaces (though problem likely guarantees none)
9        s = s.strip()
10        
11        for i, ch in enumerate(s):
12            if ch.isdigit():
13                seen_digit = True
14            elif ch in ('+', '-'):
15                # Sign is allowed only at start or right after e/E
16                if i > 0 and s[i-1] not in ('e', 'E'):
17                    return False
18            elif ch == '.':
19                # Dot is not allowed if we already saw a dot or e/E
20                if seen_dot or seen_e:
21                    return False
22                seen_dot = True
23            elif ch in ('e', 'E'):
24                # e/E is not allowed if we already saw one or no digit before it
25                if seen_e or not seen_digit:
26                    return False
27                seen_e = True
28                seen_digit = False  # Reset for exponent part (must have digits after e)
29            else:
30                # Invalid character
31                return False
32        
33        # At the end, we must have seen at least one digit
34        return seen_digit