1class Solution:
2    def rotateString(self, s: str, goal: str) -> bool:
3        # If lengths are different, it's impossible
4        if len(s) != len(goal):
5            return False
6        
7        # If both strings are empty, they are equal
8        if not s and not goal:
9            return True
10        
11        # Try all possible rotations
12        n = len(s)
13        for i in range(n):
14            # Create rotation by taking suffix starting at i + prefix up to i
15            rotated = s[i:] + s[:i]
16            if rotated == goal:
17                return True
18        
19        return False