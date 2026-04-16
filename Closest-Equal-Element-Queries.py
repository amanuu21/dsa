1from typing import List
2import bisect
3from collections import defaultdict
4
5class Solution:
6    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
7        n = len(nums)
8        
9        # Group indices by their value
10        value_to_indices = defaultdict(list)
11        for i, num in enumerate(nums):
12            value_to_indices[num].append(i)
13        
14        result = []
15        
16        for query_idx in queries:
17            target_value = nums[query_idx]
18            indices = value_to_indices[target_value]
19            
20            # If only one occurrence of this value exists
21            if len(indices) == 1:
22                result.append(-1)
23                continue
24            
25            # Find the position of query_idx in the indices list
26            pos = bisect.bisect_left(indices, query_idx)
27            
28            min_distance = float('inf')
29            
30            # Check left neighbor (previous element in indices list)
31            # Using modulo to handle circular array
32            left_pos = (pos - 1 + len(indices)) % len(indices)
33            left_idx = indices[left_pos]
34            # Calculate circular distance
35            dist = min(abs(query_idx - left_idx), n - abs(query_idx - left_idx))
36            min_distance = min(min_distance, dist)
37            
38            # Check right neighbor (next element in indices list)
39            right_pos = (pos + 1) % len(indices)
40            right_idx = indices[right_pos]
41            dist = min(abs(query_idx - right_idx), n - abs(query_idx - right_idx))
42            min_distance = min(min_distance, dist)
43            
44            result.append(min_distance)
45        
46        return result