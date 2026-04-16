1from typing import List
2
3class Solution:
4    def generateParenthesis(self, n: int) -> List[str]:
5        result = []
6        
7        def backtrack(current: str, open_count: int, close_count: int):
8            # Base case: if we've used all n pairs
9            if len(current) == 2 * n:
10                result.append(current)
11                return
12            
13            # Add opening parenthesis if we haven't used all n
14            if open_count < n:
15                backtrack(current + '(', open_count + 1, close_count)
16            
17            # Add closing parenthesis if it won't make the string invalid
18            if close_count < open_count:
19                backtrack(current + ')', open_count, close_count + 1)
20        
21        backtrack("", 0, 0)
22        return result
23
24
25# Alternative solution using iterative approach (less common but also valid)
26class Solution2:
27    def generateParenthesis(self, n: int) -> List[str]:
28        if n == 0:
29            return []
30        
31        result = []
32        stack = [("", 0, 0)]  # (current_string, open_count, close_count)
33        
34        while stack:
35            current, open_count, close_count = stack.pop()
36            
37            if len(current) == 2 * n:
38                result.append(current)
39                continue
40            
41            if open_count < n:
42                stack.append((current + '(', open_count + 1, close_count))
43            
44            if close_count < open_count:
45                stack.append((current + ')', open_count, close_count + 1))
46        
47        return result
48
49
50# Test the solution
51if __name__ == "__main__":
52    sol = Solution()
53    
54    # Example 1: n = 3
55    print(sol.generateParenthesis(3))
56    # Expected output: ["((()))","(()())","(())()","()(())","()()()"]
57    
58    # Example 2: n = 1
59    print(sol.generateParenthesis(1))
60    # Expected output: ["()"]