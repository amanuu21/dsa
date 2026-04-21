1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        if not needle:
4            return 0
5        
6        n = len(haystack)
7        m = len(needle)
8        
9        for i in range(n - m + 1):
10            if haystack[i:i + m] == needle:
11                return i
12        
13        return -1