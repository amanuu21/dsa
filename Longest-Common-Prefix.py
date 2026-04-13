1class Solution:
2    def longestCommonPrefix(self, strs):
3        if not strs:
4            return ""
5
6        prefix = strs[0]
7
8        for s in strs[1:]:
9            while not s.startswith(prefix):
10                prefix = prefix[:-1]
11                if not prefix:
12                    return ""
13
14        return prefix