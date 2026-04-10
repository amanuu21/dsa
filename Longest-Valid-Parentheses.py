1class Solution:
2    def longestValidParentheses(self, s: str) -> int:
3        stack = [-1]
4        max_len = 0
5
6        for i, char in enumerate(s):
7            if char == '(':
8                stack.append(i)
9            else:
10                stack.pop()
11
12                if not stack:
13                    stack.append(i)
14                else:
15                    max_len = max(max_len, i - stack[-1])
16
17        return max_len