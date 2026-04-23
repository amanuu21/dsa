1from collections import defaultdict
2from typing import List
3
4class Solution:
5    def distance(self, nums: List[int]) -> List[int]:
6        n = len(nums)
7        res = [0] * n
8        
9        # group indices by value
10        groups = defaultdict(list)
11        for i, v in enumerate(nums):
12            groups[v].append(i)
13        
14        # process each group
15        for indices in groups.values():
16            k = len(indices)
17            
18            # prefix sums
19            prefix = [0] * (k + 1)
20            for i in range(k):
21                prefix[i + 1] = prefix[i] + indices[i]
22            
23            for i in range(k):
24                idx = indices[i]
25                
26                # left contribution
27                left = i * idx - prefix[i]
28                
29                # right contribution
30                right = (prefix[k] - prefix[i + 1]) - (k - i - 1) * idx
31                
32                res[idx] = left + right
33        
34        return res