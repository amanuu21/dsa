1from typing import List
2from collections import Counter, defaultdict, deque
3
4class Solution:
5    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
6        n = len(source)
7        
8        # Build graph
9        graph = defaultdict(list)
10        for a, b in allowedSwaps:
11            graph[a].append(b)
12            graph[b].append(a)
13        
14        visited = [False] * n
15        components = []
16        
17        # Find connected components using BFS
18        for i in range(n):
19            if not visited[i]:
20                comp = []
21                queue = deque([i])
22                visited[i] = True
23                while queue:
24                    node = queue.popleft()
25                    comp.append(node)
26                    for nei in graph[node]:
27                        if not visited[nei]:
28                            visited[nei] = True
29                            queue.append(nei)
30                components.append(comp)
31        
32        hamming_distance = 0
33        
34        # For each component, count mismatches
35        for comp in components:
36            src_vals = [source[idx] for idx in comp]
37            tgt_vals = [target[idx] for idx in comp]
38            
39            src_counter = Counter(src_vals)
40            tgt_counter = Counter(tgt_vals)
41            
42            # Total elements in this component = len(comp)
43            # Matched = sum of min(count_src, count_tgt) over all values
44            matched = 0
45            for val, cnt_src in src_counter.items():
46                cnt_tgt = tgt_counter.get(val, 0)
47                matched += min(cnt_src, cnt_tgt)
48            
49            hamming_distance += len(comp) - matched
50        
51        return hamming_distance