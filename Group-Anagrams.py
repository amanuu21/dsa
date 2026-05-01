1from typing import List
2from collections import defaultdict
3
4class Solution:
5    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
6        groups = defaultdict(list)
7        
8        for s in strs:
9            # Sort the string to use as key
10            key = tuple(sorted(s))
11            groups[key].append(s)
12        
13        return list(groups.values())