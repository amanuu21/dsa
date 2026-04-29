1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        i = j = 0
4        star = -1
5        match = 0
6        
7        while i < len(s):
8            # direct match or '?'
9            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
10                i += 1
11                j += 1
12            
13            # '*'
14            elif j < len(p) and p[j] == '*':
15                star = j
16                match = i
17                j += 1
18            
19            # mismatch but we had '*'
20            elif star != -1:
21                j = star + 1
22                match += 1
23                i = match
24            
25            else:
26                return False
27        
28        # remaining pattern must be all '*'
29        while j < len(p) and p[j] == '*':
30            j += 1
31        
32        return j == len(p)