1class Solution:
2    def isValid(self, s):
3        stack = []
4        mapping = {
5            ')': '(',
6            '}': '{',
7            ']': '['
8        }
9
10        for char in s:
11            if char in mapping:  # closing bracket
12                top = stack.pop() if stack else '#'
13                if mapping[char] != top:
14                    return False
15            else:  # opening bracket
16                stack.append(char)
17
18        return not stack